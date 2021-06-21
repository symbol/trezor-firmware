from trezor.messages.SymbolAccountMetadata import SymbolAccountMetadata
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMosaicNamespaceMetadata import SymbolMosaicNamespaceMetadata

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm


def msg_header( meta: SymbolAccountMetadata, msg: Text):
    msg.normal("Address: %s" % meta.address)
    msg.normal("Key: %s" % meta.scoped_metadata_key)
    msg.normal("Value: %s" % meta.value.decode())
    msg.normal("Delta: %s" % meta.value_size_delta)

    return msg

async def ask_account_metadata(
    ctx,
    header: SymbolHeader,
    meta: SymbolAccountMetadata,
):
    msg = Text("Account Metadata", ui.ICON_SEND, ui.GREEN)

    msg_header(meta, msg)

    msg.normal("Max fee: %s" % header.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )


async def ask_mosaic_namespace_metadata(
    ctx,
    header: SymbolHeader,
    meta: SymbolMosaicNamespaceMetadata,
    txt: str
):
    msg = Text(txt, ui.ICON_SEND, ui.GREEN)

    msg_header(meta.header, msg)

    target_id = hex(meta.target_id)
    msg.normal("Id: %s" % target_id)

    msg.normal("Max fee: %s" % header.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )
