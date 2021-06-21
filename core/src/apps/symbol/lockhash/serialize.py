import binascii

from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolHashLock import SymbolHashLock
from trezor.messages import SymbolEntityType

from ..common_serializors import serialize_tx_header



def hash_lock(
    header: SymbolHeader,
    lock: SymbolHashLock,
) -> bytearray:

    tx = serialize_tx_header(header, SymbolEntityType.HASH_LOCK)

    write_uint64_le( tx, lock.mosaic.id )
    write_uint64_le( tx, lock.mosaic.amount )
    write_uint64_le( tx, lock.duration )
    write_bytes_unchecked( tx, binascii.unhexlify(lock.hash) )

    return tx
