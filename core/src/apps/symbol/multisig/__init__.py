from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMultisigAccountModification import SymbolMultisigAccountModification

from . import layout, serialize


async def multisig_account_modification(
    ctx, header: SymbolHeader, multisig: SymbolMultisigAccountModification
    ) -> bytearray:

    await  layout.ask_multisig_account_modification(ctx, header, multisig)
    return serialize.multisig_account_modification(header, multisig)
