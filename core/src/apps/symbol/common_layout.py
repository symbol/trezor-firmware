from micropython import const


from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_hold_to_confirm

from trezor.messages.SymbolHeader import SymbolHeader


XYM_MOSAIC_ID_MAINNET = 0x6BED913FA20223F8
SYMBOL_MAX_DIVISIBILITY = const(6)

async def require_confirm_final(ctx, header: SymbolHeader):
    if header.max_fee is not None:
        text = Text("Final confirm", ui.ICON_SEND, ui.GREEN)
        text.normal("Sign this transaction")
        text.bold("and pay %s XYM" % format_amount(header.max_fee, SYMBOL_MAX_DIVISIBILITY))
        text.normal("for network fee?")
        await require_hold_to_confirm(ctx, text, ButtonRequestType.ConfirmOutput)


def duration_to_str( duration : int ):
    if duration == 0:
        return "Unlimited"
    else:
        day_  = int(duration / 2880)
        hour_ = int((duration % 2880) / 120)
        min_ = int((duration % 120) / 2)

        return str(day_)+"d "+str(hour_)+"h "+str(min_)+"m "
