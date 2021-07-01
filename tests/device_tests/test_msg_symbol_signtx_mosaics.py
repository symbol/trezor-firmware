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

from trezorlib import symbol
from trezorlib.tools import parse_path
from trezorlib.messages import SymbolEntityType

from ..common import MNEMONIC12


# assertion data from T1
@pytest.mark.altcoin
@pytest.mark.symbol
class TestMsgSymbolSignTxMosaics:

    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_mosaic_definition(self, client):
        tx = symbol.sign_tx(
            client,
            parse_path("m/44'/1'/0'/0'/0'"),
            {
                "type": SymbolEntityType.MOSAIC_DEFINITION,

                "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                "version": 1,
                "network_type": 0x98, #public test net

                "max_fee": 2000000,
                "deadline": 26735258102,

                "id": 0x123456789A,
                "duration": 5,
                "nonce": 0x11111111,
                "flags": 5,
                "divisibility": 0
            },
        )

        assert (
            tx.data.hex()
            == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc115501984d4180841e0000000000f6a98b39060000009a785634120000000500000000000000111111110500"
        )


    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_mosaic_supply_change(self, client):
        tx = symbol.sign_tx(
            client,
            parse_path("m/44'/1'/0'/0'/0'"),
            {
                "type": SymbolEntityType.MOSAIC_SUPPLY_CHANGE,

                "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                "version": 1,
                "network_type": 0x98, #public test net
                
                "max_fee": 2000000,
                "deadline": 26735749663,

                "mosaic":{
                    "id": 0x7CDF3B117A3C40CC, #0x6BED913FA20223F8
                    "amount": 1000000,
                },
                "action": 1,
            },
        )

        assert (
            tx.data.hex()
            == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc115501984d4280841e00000000001f2a933906000000cc403c7a113bdf7c40420f000000000001"
        )
