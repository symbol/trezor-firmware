from trezor.messages import  SymbolSecretProof, SymbolTransactionCommon,SymbolSecretLock

from . import layout, serialize


async def secret_lock(
    ctx, common: SymbolTransactionCommon, lock: SymbolSecretLock
    ) -> bytearray:

    await  layout.ask_secret_lock(ctx, common, lock)
    return serialize.secret_lock(common, lock)


async def secret_proof(
    ctx, common: SymbolTransactionCommon, lock: SymbolSecretProof
    ) -> bytearray:

    await  layout.ask_secret_proof(ctx, common, lock)
    return serialize.secret_proof(common, lock)
