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
class TestMsgSymbolSignTxAggregate:
    
    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_mosaic_aggregate_complete(self, client):
        with client:
            client.set_expected_responses(
                [
                    # confirm aggregate details
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),

                    # confirm mosaic definition
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),

                    # confirm mosaic supply change
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),

                    # confirm fee
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.SymbolSignedTx,
                ]
            )

            tx = symbol.sign_tx(
                client,
                parse_path("m/44'/1'/0'/0'/0'"),
                {
                   "type": SymbolEntityType.AGGREGATE_TRANSACTION_COMPLETE,

                   "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                   "version": 1,
                   "network_type": 0x98, #public test net

                   "max_fee": 2000000,
                   "deadline": 26735656441,

                   "transactions_hash" : "e5f37fe3f83f4f0a2f21e7cf25f75cf29a20d7929cbeb7eb552eda846969281f",
                   "embedded_transactions":
                   [
                        {
                             "type": SymbolEntityType.MOSAIC_DEFINITION,
             
                             "signer_public_key" : "C4KA2RCYHRF22RGAVHNZMPRRLYOEEWTUSUTROOFY7AMTRXPHLRAA====",
                             "version": 1,
                             "network_type": 0x98, #public test net

                             "id": 0x532cb823113f2471,
                             "duration": 10,
                             "nonce": 0x440ddfea,
                             "flags": 0x7,
                             "divisibility": 0
                        },

                        {
                             "type": SymbolEntityType.MOSAIC_SUPPLY_CHANGE,
             
                             "signer_public_key" : "C4KA2RCYHRF22RGAVHNZMPRRLYOEEWTUSUTROOFY7AMTRXPHLRAA====",
                             "version": 1,
                             "network_type": 0x98, #public test net

                             "mosaic":{
                                 "id": 0x532cb823113f2471, 
                                 "amount": 1000000,
                             },
                             "action": 1,
                        }
                   ],
                   "cosignatures":
                   [
                       {
                           "version": 1,
                           "signer_public_key": "C4KA2RCYHRF22RGAVHNZMPRRLYOEEWTUSUTROOFY7AMTRXPHLRAA====",
                           "signature": "abcdef",
                       },
                       {
                           "version": 1,
                           "signer_public_key": "C4KA2RCYHRF22RGAVHNZMPRRLYOEEWTUSUTROOFY7AMTRXPHLRAB====",
                           "signature": "123456",
                       }
                   ]

                }
            )

#"0117140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c40efcdab"
#"0117140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c40563412"

            assert (
                tx.data.hex()
                == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198414180841e0000000000f9bd913906000000e5f37fe3f83f4f0a2f21e7cf25f75cf29a20d7929cbeb7eb552eda846969281f9000000000000000460000000000000017140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c400000000001984d4171243f1123b82c530a00000000000000eadf0d4407000000410000000000000017140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c400000000001984d4271243f1123b82c5340420f00000000000100000000000000010000000000000017140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c40abcdef010000000000000017140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c40123456"
            )




    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_mosaic_aggregate_bonded(self, client):
        with client:
            client.set_expected_responses(
                [
                    # confirm aggregate details
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),

                    # confirm mosaic definition
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),

                    # confirm mosaic supply change
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),

                    # confirm fee
                    proto.ButtonRequest(code=proto.ButtonRequestType.ConfirmOutput),
                    proto.SymbolSignedTx,
                ]
            )

            tx = symbol.sign_tx(
                client,
                parse_path("m/44'/1'/0'/0'/0'"),
                {
                   "type": SymbolEntityType.AGGREGATE_TRANSACTION_BONDED,

                   "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                   "version": 1,
                   "network_type": 0x98, #public test net

                   "max_fee": 2000000,
                   "deadline": 26735656441,

                   "transactions_hash" : "e5f37fe3f83f4f0a2f21e7cf25f75cf29a20d7929cbeb7eb552eda846969281f",
                   "embedded_transactions":
                   [
                        {
                             "type": SymbolEntityType.MOSAIC_DEFINITION,
             
                             "signer_public_key" : "C4KA2RCYHRF22RGAVHNZMPRRLYOEEWTUSUTROOFY7AMTRXPHLRAA====",
                             "version": 1,
                             "network_type": 0x98, #public test net

                             "id": 0x532cb823113f2471,
                             "duration": 10,
                             "nonce": 0x440ddfea,
                             "flags": 0x7,
                             "divisibility": 0
                        },

                        {
                             "type": SymbolEntityType.MOSAIC_SUPPLY_CHANGE,
             
                             "signer_public_key" : "C4KA2RCYHRF22RGAVHNZMPRRLYOEEWTUSUTROOFY7AMTRXPHLRAA====",
                             "version": 1,
                             "network_type": 0x98, #public test net

                             "mosaic":{
                                 "id": 0x532cb823113f2471, 
                                 "amount": 1000000,
                             },
                             "action": 1,
                        }
                   ]

                }
            )

            assert (
                tx.data.hex()
                == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198414180841e0000000000f9bd913906000000e5f37fe3f83f4f0a2f21e7cf25f75cf29a20d7929cbeb7eb552eda846969281f9000000000000000460000000000000017140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c400000000001984d4171243f1123b82c530a00000000000000eadf0d4407000000410000000000000017140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c400000000001984d4271243f1123b82c5340420f00000000000100000000000000"
            )



    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_delegated_harvesting(self, client):
        with client:
            client.set_expected_responses(
                [
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
                   "type": SymbolEntityType.AGGREGATE_TRANSACTION_COMPLETE,

                   "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                   "version": 1,
                   "network_type": 0x98, #public test net

                   "max_fee": 43200,
                   "deadline": 35098015682,

                   "transactions_hash" : "0c8666cef61f61b78515149a1414455c77a0ccd7c9ad5f39dfe46761ab6556df",
                   "embedded_transactions":
                   [
                        {
                             "type": SymbolEntityType.ACCOUNT_KEY_LINK,
             
                             "signer_public_key" : "C4KA2RCYHRF22RGAVHNZMPRRLYOEEWTUSUTROOFY7AMTRXPHLRAA====",
                             "version": 1,
                             "network_type": 0x98, #public test net

                             "public_key": "AATYYCANNMKJSAXBK5TSHWTDMIDF2OQTJPXGHA4CONJVIBESXEIQ====",
                             "action": 1
                        },

                        {
                             "type": SymbolEntityType.VRF_KEY_LINK,
             
                             "signer_public_key" : "C4KA2RCYHRF22RGAVHNZMPRRLYOEEWTUSUTROOFY7AMTRXPHLRAA====",
                             "version": 1,
                             "network_type": 0x98, #public test net

                             "public_key": "YGTRIMJSLBZ5QOEUS56GRR4DUTXNPIZZD2X5OBF7QUADMHWDEHNQ====",
                             "action": 1
                        },

                        {
                             "type": SymbolEntityType.NODE_KEY_LINK,
             
                             "signer_public_key" : "C4KA2RCYHRF22RGAVHNZMPRRLYOEEWTUSUTROOFY7AMTRXPHLRAA====",
                             "version": 1,
                             "network_type": 0x98, #public test net

                             "public_key": "QGEQLEXZMCVOXWTWCLEJC75JYJT2QROXRV2NJM3FDLYJHZTXKAAQ====",
                             "action": 1
                        },
                   ]
                }
            )

            assert (
                tx.data.hex()
                == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc115501984141c0a8000000000000c237012c080000000c8666cef61f61b78515149a1414455c77a0ccd7c9ad5f39dfe46761ab6556df0801000000000000510000000000000017140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c400000000001984c4100278c080d6b149902e1576723da6362065d3a134bee6383827353540492b9110100000000000000510000000000000017140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c400000000001984342c1a71431325873d83894977c68c783a4eed7a3391eafd704bf8500361ec321db0100000000000000510000000000000017140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c400000000001984c4281890592f960aaebda7612c8917fa9c267a845d78d74d4b3651af093e67750010100000000000000"
            )

    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_account_metadata_aggregate(self, client):
        with client:
            client.set_expected_responses(
                [
                    # Confirm transfer and network fee
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
                   "type": SymbolEntityType.AGGREGATE_TRANSACTION_COMPLETE,

                   "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                   "version": 1,
                   "network_type": 0x98, #public test net

                   "max_fee": 296000,
                   "deadline": 32334080719,

                   "transactions_hash" : "5f221ad2c6d297e683692ce332b24157057e6fb43a832f18c13495ec49544e08",
                   "embedded_transactions":
                   [
                        {
                             "type": SymbolEntityType.ACCOUNT_METADATA,
             
                             "signer_public_key" : "C4KA2RCYHRF22RGAVHNZMPRRLYOEEWTUSUTROOFY7AMTRXPHLRAA====",
                             "version": 1,
                             "network_type": 0x98, #public test net

                            "address": "TDZKL2HAMOWRVEEF55NVCZ7C6GSWIXCI7IWAESI=",
                            "scoped_metadata_key": 0xab8385a30dfcea7a,
                            "value_size_delta" : 43,
                            "value": b"this is the value field of account metadata".hex(),
                        },

                   ]
                }
            )

            assert (
                tx.data.hex()
                == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc1155019841414084040000000000cfea4287070000005f221ad2c6d297e683692ce332b24157057e6fb43a832f18c13495ec49544e0880000000000000007f0000000000000017140d44583c4bad44c0a9db963e315e1c425a7495271738b8f81938dde75c40000000000198444198f2a5e8e063ad1a9085ef5b5167e2f1a5645c48fa2c02497aeafc0da38583ab2b002b0074686973206973207468652076616c7565206669656c64206f66206163636f756e74206d6574616461746100"
            )
