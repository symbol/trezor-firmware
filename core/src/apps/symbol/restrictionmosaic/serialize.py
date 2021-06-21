from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMosaicAddressRestriction import SymbolMosaicAddressRestriction
from trezor.messages.SymbolMosaicGlobalRestriction import SymbolMosaicGlobalRestriction
from trezor.messages import SymbolEntityType
from trezor.crypto import base32

from ..common_serializors import serialize_tx_header

def mosaic_address_restriction(
    header: SymbolHeader, restriction: SymbolMosaicAddressRestriction
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.MOSAIC_ADDRESS_RESTRICTION)

    write_uint64_le( tx, restriction.mosaic_id )
    write_uint64_le( tx, restriction.restriction_key )
    write_uint64_le( tx, restriction.previous_restriction_value )
    write_uint64_le( tx, restriction.new_restriction_value )
    write_bytes_unchecked( tx, base32.decode(restriction.target_address) )

    return tx


def mosaic_global_restriction(
    header: SymbolHeader, restriction: SymbolMosaicGlobalRestriction
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.MOSAIC_GLOBAL_RESTRICTION)

    write_uint64_le( tx, restriction.mosaic_id )
    write_uint64_le( tx, restriction.reference_mosaic_id )
    write_uint64_le( tx, restriction.restriction_key )
    write_uint64_le( tx, restriction.previous_restriction_value )
    write_uint64_le( tx, restriction.new_restriction_value )

    write_uint8( tx, restriction.previous_restriction_type )
    write_uint8( tx, restriction.new_restriction_type )

    return tx