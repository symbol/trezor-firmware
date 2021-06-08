from trezor.messages import SymbolKeyLink, SymbolTransactionCommon, SymbolEntityType

from . import layout, serialize

def account_key_link(
    ctx, common: SymbolTransactionCommon, key_link: SymbolKeyLink
    ) -> bytearray:

    return generic(ctx, common, key_link, SymbolEntityType.ACCOUNT_KEY_LINK)


def node_key_link(
    ctx, common: SymbolTransactionCommon, key_link: SymbolKeyLink
    ) -> bytearray:

    return generic(ctx, common, key_link, SymbolEntityType.NODE_KEY_LINK)


def vrf_key_link(
    ctx, common: SymbolTransactionCommon, key_link: SymbolKeyLink
    ) -> bytearray:

    return generic(ctx, common, key_link, SymbolEntityType.VRF_KEY_LINK)


async def generic(
    ctx, common: SymbolTransactionCommon, key_link: SymbolKeyLink, entity_type: SymbolEntityType
    ) -> bytearray:

    await  layout.ask_key_link(ctx, common, key_link, entity_type)
    return serialize.key_link(common, key_link, entity_type)
