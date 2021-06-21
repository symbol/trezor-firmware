from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolAccountAddressRestriction   import SymbolAccountAddressRestriction
from trezor.messages.SymbolAccountMosaicRestriction    import SymbolAccountMosaicRestriction
from trezor.messages.SymbolAccountOperationRestriction import SymbolAccountOperationRestriction

from . import layout, serialize


async def account_address_restriction(
    ctx, header: SymbolHeader, restriction: SymbolAccountAddressRestriction
    ) -> bytearray:

    await  layout.ask_account_address_restriction(ctx, header, restriction)
    return serialize.account_address_restriction(header, restriction)


async def account_mosaic_restriction(
    ctx, header: SymbolHeader, restriction: SymbolAccountMosaicRestriction
    ) -> bytearray:

    await  layout.ask_account_mosaic_restriction(ctx, header, restriction)
    return serialize.account_mosaic_restriction(header, restriction)


async def account_operation_restriction(
    ctx, header: SymbolHeader, restriction: SymbolAccountOperationRestriction
    ) -> bytearray:

    await  layout.ask_account_operation_restriction(ctx, header, restriction)
    return serialize.account_operation_restriction(header, restriction)
