from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolNamespaceRegistration import SymbolNamespaceRegistration
from trezor.messages import SymbolAddressAlias, SymbolMosaicAlias

from . import layout, serialize


async def register(
    ctx, header: SymbolHeader, namespace_registration: SymbolNamespaceRegistration
    ) -> bytearray:

    await  layout.ask_namespace_registration(ctx, header, namespace_registration)
    return serialize.serialize_namespace_registration(header, namespace_registration)


async def address_alias(
    ctx, header: SymbolHeader, alias: SymbolAddressAlias
    ) -> bytearray:

    await  layout.ask_address_alias(ctx, header, alias)
    return serialize.serialize_address_alias(header, alias)


async def mosaic_alias(
    ctx, header: SymbolHeader, alias: SymbolMosaicAlias
    ) -> bytearray:

    await  layout.ask_mosaic_alias(ctx, header, alias)
    return serialize.serialize_mosaic_alias(header, alias)
