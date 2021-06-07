#import binascii

from trezor.crypto import base32
from trezor.messages.SymbolTransactionCommon import SymbolTransactionCommon

from apps.common.writers import write_bytes_unchecked, write_uint64_le, write_uint8, write_uint16_le


def serialize_tx_common(
    common: SymbolTransactionCommon,
    entity_type: int
) -> bytearray:
    w = bytearray()

    key = base32.decode(common.signer_public_key)
    write_bytes_unchecked(w, key)
    write_uint8(w, common.version)
    write_uint8(w, common.network_type)
    write_uint16_le(w, entity_type)
    write_uint64_le(w, common.max_fee)
    write_uint64_le(w, common.deadline)

# TODO: SYMBOL DEBUG
#    print("\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
#    print("\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
#    print(binascii.hexlify(w))
#    print("\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
#    print("\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")


    return w
