from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages.SymbolTransactionCommon import SymbolTransactionCommon
from trezor.messages.SymbolNamespaceRegistration  import SymbolNamespaceRegistration
from trezor.messages import SymbolAddressAlias, SymbolEntityType, SymbolKeyLink, SymbolVotingKeyLink
from trezor.crypto import base32

from ..common_serializors import serialize_tx_common

def key_link(
    common: SymbolTransactionCommon,
    link: SymbolKeyLink,
    entity_type: SymbolEntityType
) -> bytearray:

    tx = serialize_tx_common(common, entity_type)

    key = base32.decode(link.public_key)
    write_bytes_unchecked(tx, key)
    write_uint8(tx, link.action)

    return tx



def voting_key_link(
    common: SymbolTransactionCommon,
    link: SymbolVotingKeyLink,
) -> bytearray:

    tx = serialize_tx_common(common, SymbolEntityType.VOTING_KEY_LINK)

    key = base32.decode(link.public_key)
    write_bytes_unchecked(tx, key)
    write_uint32_le(tx, link.start_point)
    write_uint32_le(tx, link.end_point)
    write_uint8(tx, link.action)

    return tx
