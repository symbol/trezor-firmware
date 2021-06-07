from trezor.messages.SymbolTransactionCommon import SymbolTransactionCommon
from trezor.messages.SymbolMosaicDefinition import SymbolMosaicDefinition
from trezor.messages import SymbolEntityType

from . import layout, serialize

async def definition(
    ctx, common: SymbolTransactionCommon, mosaic_definition: SymbolMosaicDefinition
    ) -> bytearray:

    await  layout.ask_mosaic_definition(ctx, common, mosaic_definition)
    return serialize.serialize_mosaic_definition(common, mosaic_definition)


async def supply_change(
    ctx, common: SymbolTransactionCommon, mosaic_supply_change: SymbolMosaicDefinition
    ) -> bytearray:
    
    await  layout.ask_mosaic_supply_change(ctx, common, mosaic_supply_change)
    return serialize.serialize_mosaic_supply_change(common, mosaic_supply_change)

