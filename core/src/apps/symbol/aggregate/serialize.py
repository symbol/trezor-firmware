import binascii
#from apps import common

from trezor.messages.SymbolSignTx import SymbolSignTx
from trezor.messages import SymbolEntityType
from trezor.messages.SymbolAggregateTransaction import SymbolAggregateTransaction
from trezor.messages.SymbolHeader import SymbolHeader

from .. import transfer

from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le


from trezor.crypto import base32

from ..common_serializors import serialize_tx_header

from .. import sign_tx



async def aggregate_complete(
    ctx,
    header: SymbolHeader, aggregate: SymbolAggregateTransaction
) -> bytearray:

    ext_tx = serialize_tx_header(header, SymbolEntityType.AGGREGATE_TRANSACTION_COMPLETE)

    write_bytes_unchecked( ext_tx, binascii.unhexlify(aggregate.transactions_hash) )

    sum_int_tx_size = 0 # sum of sizes of embedded transactions with padding (in bytes)
    int_txs = bytearray()

    for etxn in aggregate.transactions:
        tmp          = await sign_tx.dispatch( ctx, etxn.header, etxn ) # serialize transaction
        len_tmp      = len(tmp)
        padding_size = 8 - (len_tmp % 8)                      # calculate padding size for 8 byte alignment
        padding      = bytearray(padding_size)                # padding bytes
   
        write_uint64_le(int_txs, len_tmp + 8)                 # size of transaction plus aggregate header
        write_bytes_unchecked(int_txs, tmp)                   # add transaction to internal transactions
        write_bytes_unchecked(int_txs, padding)               # add padding bytes to embedded transaction

        sum_int_tx_size += len_tmp + padding_size + 8


    write_uint32_le(ext_tx, sum_int_tx_size)  # payloadSize
    write_uint32_le(ext_tx, 0)                # padding
    write_bytes_unchecked(ext_tx, int_txs)    # add internal transactions

    print( ext_tx )

    return ext_tx
