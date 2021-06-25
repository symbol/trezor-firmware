from trezor.messages.SymbolHeader import SymbolHeader

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
    SymbolAddressAlias,
    SymbolNamespaceRegistration,
    SymbolMosaicAlias,
)
from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm
from apps.common.layout import split_address

from .. import common_layout


async def ask_namespace_registration(
    ctx,
    header: SymbolHeader,
    namespace: SymbolNamespaceRegistration
):

    if namespace.registration_type == 0:
        regType = "Root namespace"
    else:
        regType = "Child namespace"

    msg = Text("Namespace Reg.", ui.ICON_SEND, ui.GREEN)
    msg.normal("Name: %s"     % namespace.name)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Parameters:", ui.ICON_SEND, ui.GREEN)
    msg.normal("Type: %s"     % regType)
    msg.normal("Duration: %s" % common_layout.duration_to_str(namespace.duration))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )
    
    await common_layout.require_confirm_final(ctx, header)




async def ask_address_alias(
    ctx,
    header: SymbolHeader,
    address_alias: SymbolAddressAlias
):

    if address_alias.action == 0:
        action = "Link alias"
    else:
        action = "Unlink alias"

    msg = Text("Address Alias", ui.ICON_SEND, ui.GREEN)
    msg.normal("Action: %s"         % action)
    msg.normal("Namespace id: %s"   % hex(address_alias.namespace_id))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Address:", ui.ICON_SEND, ui.GREEN)
    msg.normal("%s"        % address_alias.address)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)


async def ask_mosaic_alias(
    ctx,
    header: SymbolHeader,
    mosaic_alias: SymbolMosaicAlias
):

    if mosaic_alias.action == 0:
        action = "Link Alias"
    else:
        action = "Unlink Alias"

    msg = Text("Mosaic Alias", ui.ICON_SEND, ui.GREEN)
    msg.normal("Action: %s"         % action)
    msg.normal("Namespace id: %s"   % hex(mosaic_alias.namespace_id))
    msg.normal("Mosaic id: %s"      % hex(mosaic_alias.mosaic_id))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)


