from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMultisigAccountModification import SymbolMultisigAccountModification

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm

from .. import common_layout



async def ask_multisig_account_modification(
    ctx,
    header: SymbolHeader,
    multisig: SymbolMultisigAccountModification,
):
    msg = Text("Multisig Acc. Mod.", ui.ICON_SEND, ui.GREEN)
    msg.normal("Number of addresses to add: %s" % len(multisig.address_additions) )
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    for address in multisig.address_additions:
        msg = Text("Add Address:", ui.ICON_SEND, ui.GREEN)
        msg.normal("%s" % address)
        await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Multisig Acc. Mod.", ui.ICON_SEND, ui.GREEN)
    msg.normal("Number of addresses to delete: %s" % len(multisig.address_deletions) )
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    for address in multisig.address_deletions:
        msg = Text("Delete Address:", ui.ICON_SEND, ui.GREEN)
        msg.normal("%s" % address)
        await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )


    msg = Text("Parameters", ui.ICON_SEND, ui.GREEN)
    msg.normal("Min Approval: %s" % multisig.min_approval_delta)
    msg.normal("Min Removal: %s" % multisig.min_removal_delta)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)