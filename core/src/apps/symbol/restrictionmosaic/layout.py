from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMosaicAddressRestriction import SymbolMosaicAddressRestriction
from trezor.messages.SymbolMosaicGlobalRestriction import SymbolMosaicGlobalRestriction

from trezor import ui
from trezor.messages import (
    ButtonRequestType
    )

from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm
from apps.common.layout import split_address



async def ask_mosaic_address_restriction(
    ctx,
    header: SymbolHeader,
    restriction: SymbolMosaicAddressRestriction
):
    msg = Text("Mosaic Address Restriction", ui.ICON_SEND, ui.GREEN)
    msg.normal("mosaic id: %s" % hex(restriction.mosaic_id))
    msg.normal("Restriction key: %s" % hex(restriction.restriction_key))
    msg.normal("Previous Restriction Value: %s" % hex(restriction.previous_restriction_value))
    msg.normal("New Restriction Value: %s" % hex(restriction.new_restriction_value))
    msg.normal("Target Address: %s" % restriction.new_restriction_value)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )


async def ask_mosaic_global_restriction(
    ctx,
    header: SymbolHeader,
    restriction: SymbolMosaicGlobalRestriction
):
    msg = Text("Mosaic Global Restriction", ui.ICON_SEND, ui.GREEN)
    msg.normal("Mosaic Id: %s" % hex(restriction.mosaic_id))
    msg.normal("Reference Mosaic ID: %s" % hex(restriction.reference_mosaic_id))
    
    msg.normal("Restriction key: %s" % hex(restriction.restriction_key))
    msg.normal("Previous Restriction Value: %s" % hex(restriction.previous_restriction_value))
    msg.normal("New Restriction Value: %s" % hex(restriction.new_restriction_value))

    msg.normal("Previous Restriction Type: %s" % restriction.previous_restriction_type)
    msg.normal("New Restriction Type: %s" % restriction.new_restriction_type)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )
