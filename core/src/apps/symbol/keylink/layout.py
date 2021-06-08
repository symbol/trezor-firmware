from trezor.messages import SymbolEntityType, SymbolTransactionCommon, SymbolKeyLink, SymbolVotingKeyLink

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm


async def ask_key_link(
    ctx,
    common: SymbolTransactionCommon,
    key_link: SymbolKeyLink,
    entity_type: SymbolEntityType
):
    if key_link.action == 0:
        action = "unlink"
    else:
        action = "link"

    if entity_type == SymbolEntityType.ACCOUNT_KEY_LINK:
        link_type = "account key"
    elif entity_type == SymbolEntityType.NODE_KEY_LINK:
        link_type = "node key"
    else:
        link_type = "vrf key"

    msg = Text("Confirm key link", ui.ICON_SEND, ui.GREEN)
    msg.normal("Type: %s" % link_type)
    msg.normal("Action: %s" % action)
    msg.normal("Linked pbk: %s" % key_link.public_key)
    msg.normal("Max fee: %s"  % common.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )


async def ask_voting_key_link(
    ctx,
    common: SymbolTransactionCommon,
    key_link: SymbolVotingKeyLink,
):
    if key_link.action == 0:
        action = "unlink"
    else:
        action = "link"

    msg = Text("Vote key link", ui.ICON_SEND, ui.GREEN)
    msg.normal("Action: %s" % action)
    msg.normal("Start: %s" % key_link.start_point)
    msg.normal("End: %s" % key_link.end_point)
    msg.normal("Pbk: %s" % key_link.public_key)
    msg.normal("Max fee: %s"  % common.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )
