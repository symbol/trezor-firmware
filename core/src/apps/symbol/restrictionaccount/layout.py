import binascii

from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolAccountAddressRestriction   import SymbolAccountAddressRestriction
from trezor.messages.SymbolAccountMosaicRestriction    import SymbolAccountMosaicRestriction
from trezor.messages.SymbolAccountOperationRestriction import SymbolAccountOperationRestriction

from trezor import ui
from trezor.messages import (
    ButtonRequestType
    )

from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm
from apps.common.layout import split_address



async def ask_account_address_restriction(
    ctx,
    header: SymbolHeader,
    restriction: SymbolAccountAddressRestriction
):

    msg = Text("Address restriction", ui.ICON_SEND, ui.GREEN)
    msg.normal("Type: %s" % restriction.type)
    
    msg.normal("Number of Additions:: %s"  % len(restriction.additions))
    for addition in restriction.additions:
        msg.normal("address: %s" % addition )

    msg.normal("Number of Deletions:: %s"  % len(restriction.deletions))
    for deletion in restriction.deletions:
        msg.normal("address: %s" % deletion )

    msg.normal("Max fee: %s" % header.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )


async def ask_account_mosaic_restriction(
    ctx,
    header: SymbolHeader,
    restriction: SymbolAccountMosaicRestriction
):

    msg = Text("Address restriction", ui.ICON_SEND, ui.GREEN)
    msg.normal("Type: %s" % restriction.type)
    
    msg.normal("Number of Additions:: %s"  % len(restriction.additions))
    for addition in restriction.additions:
        msg.normal("address: %s" % hex(addition) )

    msg.normal("Number of Deletions:: %s"  % len(restriction.deletions))
    for deletion in restriction.deletions:
        msg.normal("address: %s" % hex(deletion) )

    msg.normal("Max fee: %s" % header.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )


async def ask_account_operation_restriction(
    ctx,
    header: SymbolHeader,
    restriction: SymbolAccountOperationRestriction
):

    msg = Text("Address restriction", ui.ICON_SEND, ui.GREEN)
    msg.normal("Type: %s" % restriction.type)
    
    msg.normal("Number of Additions:: %s"  % len(restriction.additions))
    for addition in restriction.additions:
        msg.normal("address: %s" % hex(addition) )

    msg.normal("Number of Deletions:: %s"  % len(restriction.deletions))
    for deletion in restriction.deletions:
        msg.normal("address: %s" % hex(deletion) )

    msg.normal("Max fee: %s" % header.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )
