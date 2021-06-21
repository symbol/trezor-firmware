from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolAggregateTransaction import SymbolAggregateTransaction
from apps.common.writers import write_bytes_unchecked

from . import layout, serialize
from .. import sign_tx

from .. import mosaic

async def aggregate_complete(
    ctx, header: SymbolHeader, aggregate: SymbolAggregateTransaction
    ) -> bytearray:

    await layout.ask_aggregate_complete(ctx, header, aggregate)
    return await serialize.aggregate_complete(ctx, header, aggregate)
