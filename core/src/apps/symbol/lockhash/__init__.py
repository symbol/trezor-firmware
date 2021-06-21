from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolHashLock import SymbolHashLock

from . import layout, serialize


async def hash_lock(
    ctx, header: SymbolHeader, lock: SymbolHashLock
    ) -> bytearray:

    await  layout.ask_hash_lock(ctx, header, lock)
    return serialize.hash_lock(header, lock)
