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

from .. import common_layout

async def ask_mosaic_address_restriction(
    ctx,
    header: SymbolHeader,
    restriction: SymbolMosaicAddressRestriction
):
    msg = Text("Mosaic Adr. Rest.", ui.ICON_SEND, ui.GREEN)
    msg.normal("Mosaic ID: %s" % hex(restriction.mosaic_id))
    msg.normal("Restriction Key: %s" % hex(restriction.restriction_key))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Restriction Values", ui.ICON_SEND, ui.GREEN)
    msg.normal("Previous: %s" % hex(restriction.previous_restriction_value))
    msg.normal("New: %s" % hex(restriction.new_restriction_value))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Confirm Address:", ui.ICON_SEND, ui.GREEN)
    msg.normal("%s" % restriction.target_address)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header )


async def ask_mosaic_global_restriction(
    ctx,
    header: SymbolHeader,
    restriction: SymbolMosaicGlobalRestriction
):
    msg = Text("Mosaic Global Rest.", ui.ICON_SEND, ui.GREEN)
    msg.normal("Mosaic Id: %s" % hex(restriction.mosaic_id))
    msg.normal("Reference Mosaic ID: %s" % hex(restriction.reference_mosaic_id))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Restriction key:", ui.ICON_SEND, ui.GREEN)
    msg.normal("%s" % hex(restriction.restriction_key))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Restriction Values", ui.ICON_SEND, ui.GREEN)
    msg.normal("Previous: %s" % hex(restriction.previous_restriction_value))
    msg.normal("New: %s" % hex(restriction.new_restriction_value))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    int_to_string = ["No restriction", "=", "!=", "<", "<=", ">", ">="]

    msg = Text( "Restriction Types", ui.ICON_SEND, ui.GREEN )
    msg.normal( "Previous:  %s" % int_to_string[restriction.previous_restriction_type] )
    msg.normal( "New:  %s"      % int_to_string[restriction.new_restriction_type] )
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header )

