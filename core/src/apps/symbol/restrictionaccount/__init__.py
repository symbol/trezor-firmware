from trezor.messages.SymbolTransactionCommon import SymbolTransactionCommon
from trezor.messages import SymbolAccountAddressRestriction, SymbolAccountMosaicRestriction,SymbolAccountOperationRestriction

from . import layout, serialize


async def account_address_restriction(
    ctx, common: SymbolTransactionCommon, restriction: SymbolAccountAddressRestriction
    ) -> bytearray:

    await  layout.ask_account_address_restriction(ctx, common, restriction)
    return serialize.account_address_restriction(common, restriction)


async def account_mosaic_restriction(
    ctx, common: SymbolTransactionCommon, restriction: SymbolAccountMosaicRestriction
    ) -> bytearray:

    await  layout.ask_account_mosaic_restriction(ctx, common, restriction)
    return serialize.account_mosaic_restriction(common, restriction)


async def account_operation_restriction(
    ctx, common: SymbolTransactionCommon, restriction: SymbolAccountOperationRestriction
    ) -> bytearray:

    await  layout.ask_account_operation_restriction(ctx, common, restriction)
    return serialize.account_operation_restriction(common, restriction)
