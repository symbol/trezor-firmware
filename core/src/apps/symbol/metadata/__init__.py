from trezor.messages import SymbolEntityType
from trezor.messages.SymbolAccountMetadata import SymbolAccountMetadata
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMosaicNamespaceMetadata import SymbolMosaicNamespaceMetadata


from . import layout, serialize


async def account_metadata(
    ctx, header: SymbolHeader, lock: SymbolAccountMetadata
    ) -> bytearray:

    await  layout.ask_account_metadata(ctx, header, lock)
    return serialize.account_metadata(header, lock)


async def mosaic_metadata(
    ctx, header: SymbolHeader, lock: SymbolMosaicNamespaceMetadata
    ) -> bytearray:

    await  layout.ask_mosaic_namespace_metadata(ctx, header, lock, "Mosaic Metadata")
    return serialize.mosaic_namespace_metadata(header, lock, SymbolEntityType.MOSAIC_METADATA)

async def namespace_metadata(
    ctx, header: SymbolHeader, lock: SymbolMosaicNamespaceMetadata
    ) -> bytearray:

    await  layout.ask_mosaic_namespace_metadata(ctx, header, lock, "Namespace Metadata")
    return serialize.mosaic_namespace_metadata(header, lock, SymbolEntityType.NAMESPACE_METADATA)
