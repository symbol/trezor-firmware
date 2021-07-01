from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolAggregateTransaction import SymbolAggregateTransaction

from . import layout, serialize

async def aggregate_complete_bonded(
    ctx, header: SymbolHeader, aggregate: SymbolAggregateTransaction
    ) -> bytearray:

    await layout.ask_aggregate_complete_bonded(ctx, header, aggregate)
    return await serialize.aggregate_complete_bonded(ctx, header, aggregate)
