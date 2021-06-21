from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolAccountAddressRestriction   import SymbolAccountAddressRestriction
from trezor.messages.SymbolAccountMosaicRestriction    import SymbolAccountMosaicRestriction
from trezor.messages.SymbolAccountOperationRestriction import SymbolAccountOperationRestriction
from trezor.messages import SymbolEntityType
from trezor.crypto import base32

from ..common_serializors import serialize_tx_header

def account_address_restriction(
    header: SymbolHeader, restriction: SymbolAccountAddressRestriction
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.ACCOUNT_ADDRESS_RESTRICTION)

    write_uint16_le( tx, restriction.type )
    write_uint8( tx, len(restriction.additions) )
    write_uint8( tx, len(restriction.deletions) )
    write_uint32_le( tx, 0 )

    for addition in restriction.additions:
        write_bytes_unchecked( tx, base32.decode(addition) )

    for deletions in restriction.deletions:
        write_bytes_unchecked( tx, base32.decode(deletions) )

    return tx


def account_mosaic_restriction(
    header: SymbolHeader, restriction: SymbolAccountMosaicRestriction
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.ACCOUNT_MOSAIC_RESTRICTION)

    write_uint16_le( tx, restriction.type )
    write_uint8( tx, len(restriction.additions) )
    write_uint8( tx, len(restriction.deletions) )
    write_uint32_le( tx, 0 )

    for addition in restriction.additions:
        write_uint64_le( tx, addition )

    for deletions in restriction.deletions:
        write_uint64_le( tx, deletions )

    return tx


def account_operation_restriction(
    header: SymbolHeader, restriction: SymbolAccountOperationRestriction
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.ACCOUNT_OPERATION_RESTRICTION)

    write_uint16_le( tx, restriction.type )
    write_uint8( tx, len(restriction.additions) )
    write_uint8( tx, len(restriction.deletions) )
    write_uint32_le( tx, 0 )

    for addition in restriction.additions:
        write_uint16_le( tx, addition )

    for deletions in restriction.deletions:
        write_uint16_le( tx, deletions )

    return tx
