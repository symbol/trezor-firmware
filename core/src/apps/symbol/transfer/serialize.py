import binascii

from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolTransfer import SymbolTransfer
from trezor.messages import SymbolEntityType
from trezor.crypto import base32


from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from ..common_serializors import serialize_tx_header


def serialize_transfer(
    header: SymbolHeader,
    transfer: SymbolTransfer,
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.TRANSFER)

    print( transfer )

    rec_adr = base32.decode(transfer.recipient_address)
    write_bytes_unchecked(tx, rec_adr)
    write_uint16_le(tx, len(transfer.message)) #todo: no need to have message size as field
    write_uint8(tx, len(transfer.mosaics))
    write_uint32_le(tx, 0)
    write_uint8(tx, 0)

    for mosaic in transfer.mosaics:
        write_uint64_le(tx, mosaic.id)
        write_uint64_le(tx, mosaic.amount)

    write_bytes_unchecked(tx, transfer.message)

    print(binascii.hexlify(tx))


    return tx


