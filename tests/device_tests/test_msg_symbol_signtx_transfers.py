# This file is part of the Trezor project.
#
# Copyright (C) 2012-2019 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

import pytest

from trezorlib import messages as proto, symbol
from trezorlib.tools import parse_path
from trezorlib.messages import SymbolEntityType

from ..common import MNEMONIC12


# assertion data from T1
@pytest.mark.altcoin
@pytest.mark.symbol
class TestMsgSymbolSignTxTransfer:
    
    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_simple(self, client):
        with client:
            client.set_expected_responses(
                [
                    # Confirm transfer and network fee
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    # Unencrypted message
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    # Confirm recipient
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.SymbolSignedTx,
                ]
            )

            tx = symbol.sign_tx(
                client,
                parse_path("m/44'/1'/0'/0'/0'"),
                {
                   "type": SymbolEntityType.TRANSFER,

                   "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                    "version": 1,
                    "network_type": 0x98, #public test net

                    "max_fee": 2000000,
                    "deadline": 26735258102,

                    "recipient_address": "TDZKL2HAMOWRVEEF55NVCZ7C6GSWIXCI7IWAESI=",
                    "mosaics": [
                        {
                            "id": 0x091F837E059AE13C, #0x6BED913FA20223F8
                            "amount": 45000000,
                        }
                    ],
                    "message": b"\0This is a test message".hex(),
                }
            )

            assert (
                tx.data.hex()
                == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198544180841e0000000000f6a98b390600000098f2a5e8e063ad1a9085ef5b5167e2f1a5645c48fa2c024917000100000000003ce19a057e831f0940a5ae0200000000005468697320697320612074657374206d657373616765"
            )
