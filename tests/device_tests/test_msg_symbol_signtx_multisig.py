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
class TestMsgSymbolSignTxMultisig:
    
    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_multisig_account_modification(self, client):
        with client:
            client.set_expected_responses(
                [
                    # Confirm transfer and network fee
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.SymbolSignedTx,
                ]
            )

            tx = symbol.sign_tx(
                client,
                parse_path("m/44'/1'/0'/0'/0'"),
                {
                   "type": SymbolEntityType.MULTISIG_ACCOUNT_MODIFICATION,

                   "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                    "version": 1,
                    "network_type": 0x98, #public test net

                    "max_fee": 2000000,
                    "deadline": 26735258102,

                    "min_removal_delta": 1,
                    "min_approval_delta": 2,
                    "address_additions": [
                        "CEISEIRTGNCEIVKVVKVLXO6MZTO53777MZTHO4I=", #11112222333344445555AAAABBBBCCCCDDDDFFFF66667771
                        "CEISEIRTGNCEIVKVVKVLXO6MZTO53777MZTHO4Q="  #11112222333344445555AAAABBBBCCCCDDDDFFFF66667772
                    ],
                    "address_deletions": [
                        "CEISEIRTGNCEIVKVVKVLXO6MZTO53777MZTHO4Y=", #11112222333344445555AAAABBBBCCCCDDDDFFFF66667773
                    ]
                }
            )

            assert (
                tx.data.hex()
                == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198554180841e0000000000f6a98b3906000000010202010000000011112222333344445555aaaabbbbccccddddffff6666777111112222333344445555aaaabbbbccccddddffff6666777211112222333344445555aaaabbbbccccddddffff66667773"
#               == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198484180841e0000000000f6a98b3906000000 111122223333444455556666777788889999aaaabbbbccccddddeeeeffff 11112222333344445555aaaabbbbccccddddffff66667777 cc403c7a113bdf7c8096980000000000 0f00000000000000 06000000 aaaabbbbcccc"
#               == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198 4841 80841e0000000000f6a98b3906000000 cc403c7a113bdf7c80969800000000000f000000000000002b51ebcbc3e40efe8af68a0408f5a72474b1327a64e3e3b47d9b139230c7833b"
            )

#TODO: SYMBOL DEBUG
#            assert (
#                tx.signature.hex()
#                == "9cda2045324d05c791a4fc312ecceb62954e7740482f8df8928560d63cf273dea595023640179f112de755c79717757ef76962175378d6d87360ddb3f3e5f70f"
#            )

