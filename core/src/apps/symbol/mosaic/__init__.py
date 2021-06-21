from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMosaicDefinition import SymbolMosaicDefinition
from trezor.messages import SymbolEntityType

from . import layout, serialize

async def definition(
    ctx, header: SymbolHeader, mosaic_definition: SymbolMosaicDefinition
    ) -> bytearray:

    await  layout.ask_mosaic_definition(ctx, header, mosaic_definition)
    return serialize.serialize_mosaic_definition(header, mosaic_definition)


async def supply_change(
    ctx, header: SymbolHeader, mosaic_supply_change: SymbolMosaicDefinition
    ) -> bytearray:
    
    await  layout.ask_mosaic_supply_change(ctx, header, mosaic_supply_change)
    return serialize.serialize_mosaic_supply_change(header, mosaic_supply_change)

