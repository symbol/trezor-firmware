from trezor.messages import SymbolKeyLink, SymbolTransactionCommon, SymbolEntityType, SymbolHashLock

from . import layout, serialize


async def hash_lock(
    ctx, common: SymbolTransactionCommon, lock: SymbolHashLock
    ) -> bytearray:

    await  layout.ask_hash_lock(ctx, common, lock)
    return serialize.hash_lock(common, lock)
