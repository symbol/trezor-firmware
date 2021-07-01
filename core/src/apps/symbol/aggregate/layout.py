from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolAggregateTransaction import SymbolAggregateTransaction

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm
from apps.common.layout import split_address



async def ask_aggregate_complete_bonded(
    ctx,
    header: SymbolHeader,
    aggregate: SymbolAggregateTransaction
):

    msg = Text( "Agg. Transaction", ui.ICON_SEND, ui.GREEN )
    msg.bold( "Hash: %s" % aggregate.transactions_hash )
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text( "Agg. Transaction", ui.ICON_SEND, ui.GREEN )
    msg.bold( "Num of txns: %s" % len(aggregate.transactions) )
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )
