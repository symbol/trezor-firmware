from trezor.messages import SymbolTransactionCommon, SymbolMultisigAccountModification

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm



async def ask_multisig_account_modification(
    ctx,
    common: SymbolTransactionCommon,
    multisig: SymbolMultisigAccountModification,
):
    msg = Text("Multisig Account Modification", ui.ICON_SEND, ui.GREEN)

    msg.normal("Number of addresses to add: %s" % len(multisig.address_additions) )
    for address in multisig.address_additions:
        msg.normal("Address: %s" % address)

    msg.normal("Number of addresses to delete: %s" % len(multisig.address_deletions) )
    for address in multisig.address_deletions:
        msg.normal("Address: %s" % address)

    msg.normal("Min Approval: %s" % multisig.min_approval_delta)
    msg.normal("Min Removal %s" % multisig.min_removal_delta)

    msg.normal("Max fee: %s" % common.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

