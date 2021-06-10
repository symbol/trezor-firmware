from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages import SymbolEntityType, SymbolTransactionCommon, SymbolMultisigAccountModification
from trezor.crypto import base32

from ..common_serializors import serialize_tx_common



def multisig_account_modification(
    common: SymbolTransactionCommon,
    multisig: SymbolMultisigAccountModification,
) -> bytearray:

    tx = serialize_tx_common(common, SymbolEntityType.MULTISIG_ACCOUNT_MODIFICATION)

    write_uint8( tx, multisig.min_removal_delta )
    write_uint8( tx, multisig.min_approval_delta )
    write_uint8( tx, len(multisig.address_additions) )
    write_uint8( tx, len(multisig.address_deletions) )

    write_uint32_le( tx, 0 )

    for address in multisig.address_additions:
        address_raw = base32.decode( address )
        write_bytes_unchecked( tx, address_raw )

    for address in multisig.address_deletions:
        address_raw = base32.decode( address )
        write_bytes_unchecked( tx, address_raw )

    return tx
