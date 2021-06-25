import binascii

from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolAccountAddressRestriction   import SymbolAccountAddressRestriction
from trezor.messages.SymbolAccountMosaicRestriction    import SymbolAccountMosaicRestriction
from trezor.messages.SymbolAccountOperationRestriction import SymbolAccountOperationRestriction
from trezor import wire

from trezor import ui
from trezor.messages import (
    ButtonRequestType
    )

from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm
from apps.common.layout import split_address

from .. import common_layout


async def restriction_type_layout( ctx, restriction_type : int ):

    if restriction_type & 0x0001:
        msg = Text("Restriction Type:", ui.ICON_SEND, ui.GREEN)
        msg.normal("Address")
        await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    if restriction_type & 0x0002:
        msg = Text("Restriction Type:", ui.ICON_SEND, ui.GREEN)
        msg.normal("Mosaic identifier")
        await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    if restriction_type & 0x0004:
        msg = Text("Restriction type:", ui.ICON_SEND, ui.GREEN)
        msg.normal("Transaction type")
        await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    if restriction_type & 0x4000:
        msg = Text("Restriction type:", ui.ICON_SEND, ui.GREEN)
        msg.normal("Outgoing")
        await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    if restriction_type & 0x8000:
        msg = Text("Restriction type:", ui.ICON_SEND, ui.GREEN)
        msg.normal("Blocking operation")
        await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)


async def ask_restriction(
    ctx,
    header: SymbolHeader,
    restriction,
    msg : Text
):

    msg.normal("Number of Additions: %s"  % len(restriction.additions))
    await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    for addition in restriction.additions:
        msg = Text("Addition:", ui.ICON_SEND, ui.GREEN)
        msg.normal("%s" % addition)
        await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    # ------------------------------------------------------------------------

    msg = Text("Acc. Address Rest.", ui.ICON_SEND, ui.GREEN)
    msg.normal("Number of Deletions: %s" % len(restriction.deletions))
    await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    for deletion in restriction.deletions:
        msg = Text("Addition:", ui.ICON_SEND, ui.GREEN)
        msg.normal("%s" % deletion )
        await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    # ------------------------------------------------------------------------

    await restriction_type_layout(ctx, restriction.type)

    # ------------------------------------------------------------------------

    await common_layout.require_confirm_final(ctx, header )


async def ask_account_address_restriction(
    ctx,
    header: SymbolHeader,
    restriction: SymbolAccountAddressRestriction
):
    msg = Text("Acc. Address Rest.", ui.ICON_SEND, ui.GREEN)
    await ask_restriction( ctx, header, restriction, msg )



async def ask_account_mosaic_restriction(
    ctx,
    header: SymbolHeader,
    restriction: SymbolAccountMosaicRestriction
):
    msg = Text("Acc. Mosaic Rest.", ui.ICON_SEND, ui.GREEN)
    await ask_restriction( ctx, header, restriction, msg )



async def ask_account_operation_restriction(
    ctx,
    header: SymbolHeader,
    restriction: SymbolAccountOperationRestriction
):
    msg = Text("Acc. Operation Rest.", ui.ICON_SEND, ui.GREEN)
    await ask_restriction( ctx, header, restriction, msg )
