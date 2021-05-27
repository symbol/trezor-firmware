from ubinascii import hexlify

from trezor import log, wire
from trezor.messages.SymbolPublicKey import SymbolPublicKey
from trezor.messages.SymbolGetPublicKey import SymbolGetPublicKey
from trezor.messages.HDNodeType import HDNodeType
from trezor.ui.layouts import show_pubkey

from apps.common import paths
from apps.common.keychain import Keychain, auto_keychain, with_slip44_keychain
from apps.common.seed import remove_ed25519_prefix

from . import CURVE, PATTERN, SLIP44_ID


# @auto_keychain(__name__)
@with_slip44_keychain(PATTERN, slip44_id=SLIP44_ID, curve=CURVE)
async def get_public_key(
    ctx: wire.Context, msg: SymbolGetPublicKey, keychain: Keychain
) -> SymbolPublicKey:
    await paths.validate_path(
        ctx,
        keychain,
        msg.address_n,
    )

    try:
        key = _get_public_key(keychain, msg.address_n)
    except ValueError as e:
        if __debug__:
            log.exception(__name__, e)
        raise wire.ProcessError("Deriving public key failed")

    if msg.show_display:
        await show_pubkey(ctx,  hexlify(key.public_key).decode())
    return key


def _get_public_key(
    keychain: Keychain, derivation_path: list[int]
) -> SymbolPublicKey:
    node = keychain.derive(derivation_path)
    public_key = remove_ed25519_prefix(node.public_key())

    return SymbolPublicKey(public_key=public_key)

