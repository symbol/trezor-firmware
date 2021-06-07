from trezor.messages.SymbolTransactionCommon import SymbolTransactionCommon
from trezor.messages.SymbolTransfer import SymbolTransfer
from trezor.messages.SymbolMosaic import SymbolMosaic

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm
from apps.common.layout import split_address



async def ask_transfer(
    ctx,
    common: SymbolTransactionCommon,
    transfer: SymbolTransfer
):
    for mosaic in transfer.mosaics:
        await ask_transfer_mosaic(ctx, common, transfer, mosaic)

    await _require_confirm_transfer(ctx, transfer.recipient_address, len(transfer.mosaics))
    await _require_confirm_payload(ctx, transfer.message)



async def ask_transfer_mosaic(
    ctx, common: SymbolTransactionCommon, transfer: SymbolTransfer, mosaic: SymbolMosaic
):
    msg = Text("Confirm mosaic", ui.ICON_SEND, ui.GREEN)
    msg.normal("Confirm transfer of")
    msg.bold("%s units" % mosaic.amount)
    msg.normal("of")
    msg.bold("mosaic id: %s" % mosaic.id)
    await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)


async def _require_confirm_transfer(ctx, recipient, value):
    text = Text("Confirm transfer", ui.ICON_SEND, ui.GREEN)
    text.bold("Send %s XYM" % value)
    text.normal("to")
    text.mono(*split_address(recipient))
    await require_confirm(ctx, text, ButtonRequestType.ConfirmOutput)


async def _require_confirm_payload(ctx, payload: bytearray):
    message_type = payload[0]
    message_payload = payload[1:]
    message_payload = bytes(message_payload).decode()


    text = Text("Confirm payload", ui.ICON_SEND, ui.GREEN)
    text.bold("Message type: %s" % message_type)
    text.normal("Payload message: %s" % message_payload)

#    text = Text("Confirm payload", ui.ICON_SEND, ui.GREEN)
#    text.bold("Message type: %s", "HOLA1")
#    text.normal("Payload message: %s", "message_payload")


# TODO: SYMBOL DEBUG
#    print("\n\n\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
#    print( text.read_content() )
#    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\n\n")

    await require_confirm(ctx, text, ButtonRequestType.ConfirmOutput)
