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
class TestMsgSymbolSignTxMetadata:
    
    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_account_metadata(self, client):
        with client:
            client.set_expected_responses(
                [
                    # Confirm transfer and network fee
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
                   "type": SymbolEntityType.ACCOUNT_METADATA,

                   "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                    "version": 1,
                    "network_type": 0x98, #public test net

                    "max_fee": 2000000,
                    "deadline": 26735258102,

                    "address": "CEISEIRTGNCEIVKVVKVLXO6MZTO53777MZTHO5Y=", #11112222333344445555AAAABBBBCCCCDDDDFFFF66667777
                    "scoped_metadata_key": 0x1111222233334444,
                    "value_size_delta" : 39,
                    "value": b"value field of account metadata".hex(),
                }
            )

            assert (
                tx.data.hex()
                == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198444180841e0000000000f6a98b390600000011112222333344445555aaaabbbbccccddddffff66667777444433332222111127001f0076616c7565206669656c64206f66206163636f756e74206d65746164617461"
#               == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198484180841e0000000000f6a98b3906000000 111122223333444455556666777788889999aaaabbbbccccddddeeeeffff 11112222333344445555aaaabbbbccccddddffff66667777 cc403c7a113bdf7c8096980000000000 0f00000000000000 06000000 aaaabbbbcccc"
#               == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198 4841 80841e0000000000f6a98b3906000000 cc403c7a113bdf7c80969800000000000f000000000000002b51ebcbc3e40efe8af68a0408f5a72474b1327a64e3e3b47d9b139230c7833b"
            )

#TODO: SYMBOL DEBUG
#            assert (
#                tx.signature.hex()
#                == "9cda2045324d05c791a4fc312ecceb62954e7740482f8df8928560d63cf273dea595023640179f112de755c79717757ef76962175378d6d87360ddb3f3e5f70f"
#            )






    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_mosaic_metadata(self, client):
        with client:
            client.set_expected_responses(
                [
                    # Confirm transfer and network fee
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
                   "type": SymbolEntityType.MOSAIC_METADATA,

                   "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                    "version": 1,
                    "network_type": 0x98, #public test net

                    "max_fee": 2000000,
                    "deadline": 26735258102,

                    "address": "CEISEIRTGNCEIVKVVKVLXO6MZTO53777MZTHO5Y=", #11112222333344445555AAAABBBBCCCCDDDDFFFF66667777
                    "scoped_metadata_key": 0x1111222233334444,
                    "target_id": 0x123456789ABCDEF0,
                    "value_size_delta" : 39,
                    "value": b"value field of account metadata".hex(),
                }
            )

            assert (
                tx.data.hex()
                == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198444280841e0000000000f6a98b390600000011112222333344445555aaaabbbbccccddddffff666677774444333322221111f0debc9a7856341227001f0076616c7565206669656c64206f66206163636f756e74206d65746164617461"
#               == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198484180841e0000000000f6a98b3906000000 111122223333444455556666777788889999aaaabbbbccccddddeeeeffff 11112222333344445555aaaabbbbccccddddffff66667777 cc403c7a113bdf7c8096980000000000 0f00000000000000 06000000 aaaabbbbcccc"
#               == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198 4841 80841e0000000000f6a98b3906000000 cc403c7a113bdf7c80969800000000000f000000000000002b51ebcbc3e40efe8af68a0408f5a72474b1327a64e3e3b47d9b139230c7833b"
            )

#TODO: SYMBOL DEBUG
#            assert (
#                tx.signature.hex()
#                == "9cda2045324d05c791a4fc312ecceb62954e7740482f8df8928560d63cf273dea595023640179f112de755c79717757ef76962175378d6d87360ddb3f3e5f70f"
#            )

    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_symbol_signtx_namespace_metadata(self, client):
        with client:
            client.set_expected_responses(
                [
                    # Confirm transfer and network fee
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
                   "type": SymbolEntityType.NAMESPACE_METADATA,

                   "signer_public_key" : "HNPB7JSEKZJ4S4NFA2D6OXTNBH5TASAQKXRZSDEEWJPJEIW4CFKQ====",
                    "version": 1,
                    "network_type": 0x98, #public test net

                    "max_fee": 2000000,
                    "deadline": 26735258102,

                    "address": "CEISEIRTGNCEIVKVVKVLXO6MZTO53777MZTHO5Y=", #11112222333344445555AAAABBBBCCCCDDDDFFFF66667777
                    "scoped_metadata_key": 0x1111222233334444,
                    "target_id": 0x123456789ABCDEF0,
                    "value_size_delta" : 39,
                    "value": b"value field of account metadata".hex(),
                }
            )

            assert (
                tx.data.hex()
                == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198444380841e0000000000f6a98b390600000011112222333344445555aaaabbbbccccddddffff666677774444333322221111f0debc9a7856341227001f0076616c7565206669656c64206f66206163636f756e74206d65746164617461"
#               == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198484180841e0000000000f6a98b3906000000 111122223333444455556666777788889999aaaabbbbccccddddeeeeffff 11112222333344445555aaaabbbbccccddddffff66667777 cc403c7a113bdf7c8096980000000000 0f00000000000000 06000000 aaaabbbbcccc"
#               == "3b5e1fa6445653c971a50687e75e6d09fb30481055e3990c84b25e9222dc11550198 4841 80841e0000000000f6a98b3906000000 cc403c7a113bdf7c80969800000000000f000000000000002b51ebcbc3e40efe8af68a0408f5a72474b1327a64e3e3b47d9b139230c7833b"
            )

#TODO: SYMBOL DEBUG
#            assert (
#                tx.signature.hex()
#                == "9cda2045324d05c791a4fc312ecceb62954e7740482f8df8928560d63cf273dea595023640179f112de755c79717757ef76962175378d6d87360ddb3f3e5f70f"
#            )