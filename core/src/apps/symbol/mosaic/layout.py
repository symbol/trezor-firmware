from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMosaicDefinition import SymbolMosaicDefinition
from trezor.messages.SymbolMosaicSupplyChange import SymbolMosaicSupplyChange
from trezor.strings import format_amount

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm
from apps.common.layout import split_address

from .. import common_layout



async def ask_mosaic_definition(
    ctx,
    header: SymbolHeader,
    definition: SymbolMosaicDefinition
):
    msg = Text("Mosaic Definition", ui.ICON_SEND, ui.GREEN)
    msg.bold("Id: %s"    % hex(definition.id))
    msg.bold("Divisibility: %s" % definition.divisibility)
    msg.bold("Duration: %s"     % common_layout.duration_to_str(definition.duration))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Parameters:", ui.ICON_SEND, ui.GREEN)
    msg.bold("Mutable: %s"      % bool(definition.flags & 0x01))
    msg.bold("Transferable: %s" % bool(definition.flags & 0x02))
    msg.bold("Restrictable: %s" % bool(definition.flags & 0x04))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)


async def ask_mosaic_supply_change(
    ctx,
    header: SymbolHeader,
    supply: SymbolMosaicSupplyChange
):
    if supply.action == 0:
        action = "Increase"
    else:
        action = "Decrease"

    msg = Text("Mosaic Sup. Change", ui.ICON_SEND, ui.GREEN)
    msg.normal("Mosaic id: %s" % hex(supply.mosaic.id))
    msg.normal("%s by" % action)
    msg.bold("%s units" % format_amount(supply.mosaic.amount, common_layout.SYMBOL_MAX_DIVISIBILITY))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)




        




