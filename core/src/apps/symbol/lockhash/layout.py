from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolHashLock import SymbolHashLock
from trezor.strings import format_amount

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm

from .. import common_layout


async def ask_hash_lock(
    ctx,
    header: SymbolHeader,
    lock: SymbolHashLock,
):
    msg = Text("Hash lock", ui.ICON_SEND, ui.GREEN)
    msg.normal("Lock Quantity: %s XYM" % format_amount(lock.mosaic.amount, common_layout.SYMBOL_MAX_DIVISIBILITY))
    msg.normal("Duration: %s"      % common_layout.duration_to_str(lock.duration))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Tx hash", ui.ICON_SEND, ui.GREEN)
    msg.normal("%s"       % lock.hash)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)

