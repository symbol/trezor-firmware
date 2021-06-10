from trezor.messages import SymbolKeyLink, SymbolTransactionCommon, SymbolMultisigAccountModification

from . import layout, serialize


async def multisig_account_modification(
    ctx, common: SymbolTransactionCommon, multisig: SymbolMultisigAccountModification
    ) -> bytearray:

    await  layout.ask_multisig_account_modification(ctx, common, multisig)
    return serialize.multisig_account_modification(common, multisig)
