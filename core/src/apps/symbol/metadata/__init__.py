from trezor.messages import  SymbolTransactionCommon, SymbolAccountMetadata, SymbolMosaicNamespaceMetadata, SymbolEntityType

from . import layout, serialize


async def account_metadata(
    ctx, common: SymbolTransactionCommon, lock: SymbolAccountMetadata
    ) -> bytearray:

    await  layout.ask_account_metadata(ctx, common, lock)
    return serialize.account_metadata(common, lock)


async def mosaic_metadata(
    ctx, common: SymbolTransactionCommon, lock: SymbolMosaicNamespaceMetadata
    ) -> bytearray:

    await  layout.ask_mosaic_namespace_metadata(ctx, common, lock, "Mosaic Metadata")
    return serialize.mosaic_namespace_metadata(common, lock, SymbolEntityType.MOSAIC_METADATA)

async def namespace_metadata(
    ctx, common: SymbolTransactionCommon, lock: SymbolMosaicNamespaceMetadata
    ) -> bytearray:

    await  layout.ask_mosaic_namespace_metadata(ctx, common, lock, "Namespace Metadata")
    return serialize.mosaic_namespace_metadata(common, lock, SymbolEntityType.NAMESPACE_METADATA)
