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
class TestMsgSymbolSignTxNamespace:

    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_namespace_registration(self, client):
        tx = symbol.sign_tx(
            client,
            parse_path("m/44'/1'/0'/0'/0'"),
            {
                "type": SymbolEntityType.NAMESPACE_REGISTRATION,

                "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                "version": 1,
                "network_type": 0x98, #public test net

                "max_fee": 2000000,
                "deadline": 29061842962,

                "duration": 172800,
                "parent_id": 675,
                "id": 12215251730993545416,
                "registration_type": 0,
                "name": "foo576sgnlxdnfbdx",
            },
        )

        assert (
            tx.data.hex()
            == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc115501984e4180841e0000000000128838c40600000000a3020000000000c880d8ebba4a85a90011666f6f35373673676e6c78646e66626478"
        )
#        assert (
#            tx.signature.hex()
#            == "928b03c4a69fff35ecf0912066ea705895b3028fad141197d7ea2b56f1eef2a2516455e6f35d318f6fa39e2bb40492ac4ae603260790f7ebc7ea69feb4ca4c0a"
#        ) TODO: SYMBOL DEBUG



    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_address_alias(self, client):
        tx = symbol.sign_tx(
            client,
            parse_path("m/44'/1'/0'/0'/0'"),
            {
                "type": SymbolEntityType.ADDRESS_ALIAS,

                "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                "version": 1,
                "network_type": 0x98, #public test net

                "max_fee": 2000000,
                "deadline": 26736012201,

                "namespace_id": 0x82A9D1AC587EC054,
                "address": "TDZKL2HAMOWRVEEF55NVCZ7C6GSWIXCI7IWAESI=",
                "action": 1,
            },
        )

        assert (
            tx.data.hex()
            == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc115501984e4280841e0000000000a92b97390600000054c07e58acd1a98298f2a5e8e063ad1a9085ef5b5167e2f1a5645c48fa2c024901"
        )
#        assert (
#            tx.signature.hex()
#            == "928b03c4a69fff35ecf0912066ea705895b3028fad141197d7ea2b56f1eef2a2516455e6f35d318f6fa39e2bb40492ac4ae603260790f7ebc7ea69feb4ca4c0a"
#        ) TODO: SYMBOL DEBUG
