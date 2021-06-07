import binascii


from trezor.messages.SymbolTransactionCommon import SymbolTransactionCommon

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
    SymbolAddressAlias,
    SymbolNamespaceRegistration,
)
from trezor.strings import format_amount
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm
from apps.common.layout import split_address



async def ask_namespace_registration(
    ctx,
    common: SymbolTransactionCommon,
    namespace: SymbolNamespaceRegistration
):

    if namespace.registration_type == 0:
        regType = "Root namespace"
    else:
        regType = "Child namespace"

    msg = Text("Namespace registration", ui.ICON_SEND, ui.GREEN)
    msg.normal("Type: %s"     % regType)
    msg.normal("Name: %s"     % namespace.name)
    msg.normal("Duration: %s" % namespace.duration)
    msg.normal("Max fee: %s"  % common.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )



async def ask_address_alias(
    ctx,
    common: SymbolTransactionCommon,
    address_alias: SymbolAddressAlias
):

    if address_alias.action == 0:
        action = "Link alias"
    else:
        action = "Unlink alias"

    msg = Text("Address alias", ui.ICON_SEND, ui.GREEN)
    msg.normal("Action: %s"         % action)
    msg.normal("Namespace id: %s"   % hex(address_alias.namespace_id))
    msg.normal("Address: %s"        % address_alias.address)
    msg.normal("max fee: %s"        % common.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )



