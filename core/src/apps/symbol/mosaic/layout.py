from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMosaicDefinition import SymbolMosaicDefinition
from trezor.messages.SymbolMosaicSupplyChange import SymbolMosaicSupplyChange

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm
from apps.common.layout import split_address



async def ask_mosaic_definition(
    ctx,
    header: SymbolHeader,
    definition: SymbolMosaicDefinition
):
    msg = Text("Confirm mosaic definition", ui.ICON_SEND, ui.GREEN)
    msg.bold("mosaic id: %s"    % definition.id)
    msg.bold("divisibility: %s" % definition.divisibility)
    msg.bold("duration: %s"     % definition.duration)
    msg.bold("mutable: %s"      % bool(definition.flags & 0x01))
    msg.bold("transferable: %s" % bool(definition.flags & 0x02))
    msg.bold("restrictable: %s" % bool(definition.flags & 0x04))

    if hasattr(header, "max_fee"):
        msg.bold( "max fee: %s"  % header.max_fee)
        msg.bold( "deadline: %s" % header.deadline)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )
    

async def ask_mosaic_supply_change(
    ctx,
    header: SymbolHeader,
    supply: SymbolMosaicSupplyChange
):
    if supply.action == 0:
        action = "increase"
    else:
        action = "decrease"

    msg = Text("Confirm mosaic supply change", ui.ICON_SEND, ui.GREEN)
    msg.bold("mosaic id: %s" % supply.mosaic.id)
    msg.normal("%s by" % action)
    msg.bold("%s units" % supply.mosaic.amount)

    if hasattr(header, "max_fee"):
        msg.bold("max fee: %s" % header.max_fee)
        msg.bold("deadline: %s" % header.deadline)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )


        




