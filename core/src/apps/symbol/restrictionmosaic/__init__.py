from trezor.messages.SymbolTransactionCommon import SymbolTransactionCommon
from trezor.messages import SymbolMosaicAddressRestriction, SymbolMosaicGlobalRestriction

from . import layout, serialize


async def mosaic_address_restriction(
    ctx, common: SymbolTransactionCommon, restriction: SymbolMosaicAddressRestriction
    ) -> bytearray:

    await  layout.ask_mosaic_address_restriction(ctx, common, restriction)
    return serialize.mosaic_address_restriction(common, restriction)


async def mosaic_global_restriction(
    ctx, common: SymbolTransactionCommon, restriction: SymbolMosaicGlobalRestriction
    ) -> bytearray:

    await  layout.ask_mosaic_global_restriction(ctx, common, restriction)
    return serialize.mosaic_global_restriction(common, restriction)
