import binascii

from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages import SymbolEntityType, SymbolHashLock, SymbolTransactionCommon

from ..common_serializors import serialize_tx_common



def hash_lock(
    common: SymbolTransactionCommon,
    lock: SymbolHashLock,
) -> bytearray:

    tx = serialize_tx_common(common, SymbolEntityType.HASH_LOCK)

    write_uint64_le( tx, lock.mosaic.id )
    write_uint64_le( tx, lock.mosaic.amount )
    write_uint64_le( tx, lock.duration )
    write_bytes_unchecked( tx, binascii.unhexlify(lock.hash) )

    return tx
