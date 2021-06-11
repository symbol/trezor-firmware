from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages.SymbolTransactionCommon import SymbolTransactionCommon
from trezor.messages.SymbolNamespaceRegistration  import SymbolNamespaceRegistration
from trezor.messages import SymbolEntityType, SymbolAccountAddressRestriction, SymbolAccountMosaicRestriction, SymbolAccountOperationRestriction
from trezor.crypto import base32

from ..common_serializors import serialize_tx_common

def account_address_restriction(
    common: SymbolTransactionCommon, restriction: SymbolAccountAddressRestriction
) -> bytearray:
    tx = serialize_tx_common(common, SymbolEntityType.ACCOUNT_ADDRESS_RESTRICTION)

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
    common: SymbolTransactionCommon, restriction: SymbolAccountMosaicRestriction
) -> bytearray:
    tx = serialize_tx_common(common, SymbolEntityType.ACCOUNT_MOSAIC_RESTRICTION)

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
    common: SymbolTransactionCommon, restriction: SymbolAccountOperationRestriction
) -> bytearray:
    tx = serialize_tx_common(common, SymbolEntityType.ACCOUNT_OPERATION_RESTRICTION)

    write_uint16_le( tx, restriction.type )
    write_uint8( tx, len(restriction.additions) )
    write_uint8( tx, len(restriction.deletions) )
    write_uint32_le( tx, 0 )

    for addition in restriction.additions:
        write_uint16_le( tx, addition )

    for deletions in restriction.deletions:
        write_uint16_le( tx, deletions )

    return tx
