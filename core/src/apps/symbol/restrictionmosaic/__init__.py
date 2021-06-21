from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMosaicAddressRestriction import SymbolMosaicAddressRestriction
from trezor.messages.SymbolMosaicGlobalRestriction import SymbolMosaicGlobalRestriction

from . import layout, serialize


async def mosaic_address_restriction(
    ctx, header: SymbolHeader, restriction: SymbolMosaicAddressRestriction
    ) -> bytearray:

    await  layout.ask_mosaic_address_restriction(ctx, header, restriction)
    return serialize.mosaic_address_restriction(header, restriction)


async def mosaic_global_restriction(
    ctx, header: SymbolHeader, restriction: SymbolMosaicGlobalRestriction
    ) -> bytearray:

    await  layout.ask_mosaic_global_restriction(ctx, header, restriction)
    return serialize.mosaic_global_restriction(header, restriction)
