from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolTransfer import SymbolTransfer
from trezor.messages.SymbolMosaic import SymbolMosaic

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm, require_hold_to_confirm
from apps.common.layout import split_address

from .. import common_layout

#import binascii

async def ask_transfer(
    ctx,
    header: SymbolHeader,
    transfer: SymbolTransfer
):
    for mosaic in transfer.mosaics:
        await ask_transfer_mosaic(ctx, header, transfer, mosaic)

    await _require_confirm_transfer(ctx, transfer.recipient_address, len(transfer.mosaics))
    await _require_confirm_payload(ctx, transfer.message)
    await common_layout.require_confirm_final(ctx, header )



async def ask_transfer_mosaic(
    ctx, header: SymbolHeader, transfer: SymbolTransfer, mosaic: SymbolMosaic
):
    msg = Text("Confirm Transfer", ui.ICON_SEND, ui.GREEN)
    msg.normal("Confirm transfer of")
    msg.bold("%s units" % format_amount(mosaic.amount, common_layout.SYMBOL_MAX_DIVISIBILITY))
    msg.normal("of")

    if mosaic.id == common_layout.XYM_MOSAIC_ID_MAINNET:
        msg.bold("XYM")
    else:
        msg.bold( "mosaic id: %s" % hex(mosaic.id) )

    await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)


async def _require_confirm_transfer(ctx, recipient, value):
    text = Text("Confirm Address", ui.ICON_SEND, ui.GREEN)
    text.normal("Send to:")
    text.bold(*split_address(recipient))
    await require_confirm(ctx, text, ButtonRequestType.ConfirmOutput)


async def _require_confirm_payload(ctx, payload: bytearray):
    message_type = payload[0]
    message_payload = payload[1:]
    message_payload = bytes(message_payload).decode()

    text = Text("Confirm payload", ui.ICON_SEND, ui.GREEN)

    int_to_string = ["Plain message", "Encrypted message", "Persistent harvesting delegation"]
    text.normal("%s:" % int_to_string[message_type])
    text.bold("%s" % message_payload)

    await require_confirm(ctx, text, ButtonRequestType.ConfirmOutput)


