from trezor.messages.SymbolTransactionCommon import SymbolTransactionCommon
from trezor.messages.SymbolNamespaceRegistration import SymbolNamespaceRegistration
from trezor.messages import SymbolAddressAlias

from . import layout, serialize


async def register(
    ctx, common: SymbolTransactionCommon, namespace_registration: SymbolNamespaceRegistration
    ) -> bytearray:

    await  layout.ask_namespace_registration(ctx, common, namespace_registration)
    return serialize.serialize_namespace_registration(common, namespace_registration)


async def address_alias(
    ctx, common: SymbolTransactionCommon, alias: SymbolAddressAlias
    ) -> bytearray:

    await  layout.ask_address_alias(ctx, common, alias)
    return serialize.serialize_address_alias(common, alias)
