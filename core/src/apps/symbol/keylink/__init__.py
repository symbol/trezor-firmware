from trezor.messages import SymbolEntityType
from trezor.messages.SymbolKeyLink import SymbolKeyLink
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolVotingKeyLink import SymbolVotingKeyLink

from . import layout, serialize

def account_key_link(
    ctx, header: SymbolHeader, key_link: SymbolKeyLink
    ) -> bytearray:

    return generic(ctx, header, key_link, SymbolEntityType.ACCOUNT_KEY_LINK)


def node_key_link(
    ctx, header: SymbolHeader, key_link: SymbolKeyLink
    ) -> bytearray:

    return generic(ctx, header, key_link, SymbolEntityType.NODE_KEY_LINK)


def vrf_key_link(
    ctx, header: SymbolHeader, key_link: SymbolKeyLink
    ) -> bytearray:

    return generic(ctx, header, key_link, SymbolEntityType.VRF_KEY_LINK)


async def voting_key_link(
    ctx, header: SymbolHeader, key_link: SymbolVotingKeyLink
    ) -> bytearray:

    await  layout.ask_voting_key_link(ctx, header, key_link)
    return serialize.voting_key_link(header, key_link)



async def generic(
    ctx, header: SymbolHeader, key_link: SymbolKeyLink, entity_type: SymbolEntityType
    ) -> bytearray:

    await  layout.ask_key_link(ctx, header, key_link, entity_type)
    return serialize.key_link(header, key_link, entity_type)
