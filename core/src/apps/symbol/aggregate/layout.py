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



async def ask_aggregate_complete(
    ctx,
    header: SymbolHeader,
    aggregate: SymbolAggregateTransaction
):

    msg = Text( "Aggregate transaction", ui.ICON_SEND, ui.GREEN )
    msg.bold( "Hash: %s" % aggregate.transactions_hash )
    msg.bold( "Num of txns: %s" % len(aggregate.transactions) )

    msg.bold( "max fee: %s" % header.max_fee )
    msg.bold( "deadline: %s" % header.deadline )

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )
