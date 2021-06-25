from trezor.messages import SymbolEntityType, SymbolHeader, SymbolKeyLink, SymbolVotingKeyLink
from trezor import wire

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm

from .. import common_layout


async def ask_key_link(
    ctx,
    header: SymbolHeader,
    key_link: SymbolKeyLink,
    entity_type: SymbolEntityType
):
    if key_link.action == 0:
        action = "Unlink"
    elif key_link.action == 1:
        action = "Link"
    else:
        raise wire.DataError("Invalid key link action")

    if entity_type == SymbolEntityType.ACCOUNT_KEY_LINK:
        msg = Text("Account Key Link", ui.ICON_SEND, ui.GREEN)
    elif entity_type == SymbolEntityType.NODE_KEY_LINK:
        msg = Text("Node Key Link", ui.ICON_SEND, ui.GREEN)
    elif entity_type == SymbolEntityType.VRF_KEY_LINK:
        msg = Text("Vrf Key Link", ui.ICON_SEND, ui.GREEN)
    else:
        raise wire.DataError("Invalid entity_type")

    msg.normal("Action: %s" % action)
    msg.normal("Linked pbk: %s" % key_link.public_key)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)


async def ask_voting_key_link(
    ctx,
    header: SymbolHeader,
    key_link: SymbolVotingKeyLink,
):
    if key_link.action == 0:
        action = "Unlink"
    elif key_link.action == 1:
        action = "Link"
    else:
        raise wire.DataError("Invalid key link action")

    msg = Text("Vote key link", ui.ICON_SEND, ui.GREEN)
    msg.normal("Action: %s" % action)
    msg.normal("Start Point: %s" % key_link.start_point)
    msg.normal("End Point: %s" % key_link.end_point)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Vote key link", ui.ICON_SEND, ui.GREEN)
    msg.normal("Public Key: %s" % key_link.public_key)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)
