from trezor.messages.SymbolSecretProof import SymbolSecretProof
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolSecretLock import SymbolSecretLock

from . import layout, serialize


async def secret_lock(
    ctx, header: SymbolHeader, lock: SymbolSecretLock
    ) -> bytearray:

    await  layout.ask_secret_lock(ctx, header, lock)
    return serialize.secret_lock(header, lock)


async def secret_proof(
    ctx, header: SymbolHeader, lock: SymbolSecretProof
    ) -> bytearray:

    await  layout.ask_secret_proof(ctx, header, lock)
    return serialize.secret_proof(header, lock)
