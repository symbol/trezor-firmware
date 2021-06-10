import binascii

from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages import SymbolEntityType, SymbolAccountMetadata, SymbolTransactionCommon
from trezor.crypto import base32

from ..common_serializors import serialize_tx_common



def account_metadata(
    common: SymbolTransactionCommon,
    metadata: SymbolAccountMetadata,
) -> bytearray:

    tx = serialize_tx_common(common, SymbolEntityType.ACCOUNT_METADATA)

    address = base32.decode( metadata.address )
    write_bytes_unchecked( tx, address )
    write_uint64_le( tx, metadata.scoped_metadata_key )
    write_uint16_le( tx, metadata.value_size_delta )
    write_uint16_le( tx, len(metadata.value))
    write_bytes_unchecked( tx, metadata.value )
    return tx


def mosaic_namespace_metadata(
    common: SymbolTransactionCommon,
    metadata: SymbolAccountMetadata,
    entity_type: SymbolEntityType
) -> bytearray:

    tx = serialize_tx_common( common, entity_type )

    address = base32.decode( metadata.header.address )
    write_bytes_unchecked( tx, address )
    write_uint64_le( tx, metadata.header.scoped_metadata_key )

    write_uint64_le( tx, metadata.target_id )

    write_uint16_le( tx, metadata.header.value_size_delta )
    write_uint16_le( tx, len(metadata.header.value) )
    write_bytes_unchecked( tx, metadata.header.value )

    return tx
