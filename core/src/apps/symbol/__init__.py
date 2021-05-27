from trezor import wire
from trezor.messages import MessageType

# from apps.common.paths import PATTERN_BIP44_PUBKEY

CURVE = "ed25519"
SLIP44_ID = 4343
PATTERN = "m/44'/coin_type'/account'/change'/address_index'"


#def boot() -> None:
#    wire.add(MessageType.SymbolGetPublicKey, __name__, "get_public_key")