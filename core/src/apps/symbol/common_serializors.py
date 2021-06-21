#import binascii

from trezor.crypto import base32
from trezor.messages.SymbolHeader import SymbolHeader

from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le


def serialize_tx_header(
    header: SymbolHeader,
    entity_type: int
) -> bytearray:
    w = bytearray()

    key = base32.decode(header.signer_public_key)
    write_bytes_unchecked(w, key)

    if header.max_fee is None:
        write_uint32_le(w, 0) # padding (only in case of aggregate transactions)

    write_uint8(w, header.version)
    write_uint8(w, header.network_type)
    write_uint16_le(w, entity_type)

    if header.max_fee is not None:
        write_uint64_le(w, header.max_fee)
        write_uint64_le(w, header.deadline)


    return w
