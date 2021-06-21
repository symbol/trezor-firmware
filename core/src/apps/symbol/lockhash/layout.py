from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolHashLock import SymbolHashLock

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm



async def ask_hash_lock(
    ctx,
    header: SymbolHeader,
    lock: SymbolHashLock,
):
    msg = Text("Hash lock", ui.ICON_SEND, ui.GREEN)
    msg.normal("Lock Quantity: %s" % lock.mosaic.amount)
    msg.normal("Duration: %s"      % lock.duration)
    msg.normal("Tx hash: %s"       % lock.hash)
#    msg.normal("Max fee: %s"       % header.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )
