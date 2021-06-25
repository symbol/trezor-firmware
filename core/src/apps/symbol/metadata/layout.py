from trezor.messages.SymbolAccountMetadata import SymbolAccountMetadata
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMosaicNamespaceMetadata import SymbolMosaicNamespaceMetadata

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm

from .. import common_layout

async def msg_header( ctx, meta: SymbolAccountMetadata, msg: Text):
    msg.normal("Address: %s" % meta.address)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Fields", ui.ICON_SEND, ui.GREEN)
    msg.normal("Key: %s" % hex(meta.scoped_metadata_key))
    msg.normal("Value: %s" % meta.value.decode())
    msg.normal("Delta: %s" % meta.value_size_delta)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    return msg

async def ask_account_metadata(
    ctx,
    header: SymbolHeader,
    meta: SymbolAccountMetadata,
):
    msg = Text("Account Metadata", ui.ICON_SEND, ui.GREEN)

    await msg_header(ctx, meta, msg)
    await common_layout.require_confirm_final(ctx, header)


async def ask_mosaic_namespace_metadata(
    ctx,
    header: SymbolHeader,
    meta: SymbolMosaicNamespaceMetadata,
    txt: str
):
    msg = Text(txt, ui.ICON_SEND, ui.GREEN)

    await msg_header(ctx, meta.header, msg)


    msg = Text(txt, ui.ICON_SEND, ui.GREEN)
    target_id = hex(meta.target_id)
    msg.normal("Id: %s" % target_id)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)

