from trezor.messages.SymbolTransactionCommon import SymbolTransactionCommon
from trezor.messages.SymbolTransfer import SymbolTransfer
from trezor.messages import SymbolEntityType


from apps.common.writers import write_bytes_unchecked, write_uint16_le, write_uint32_le, write_uint64_le, write_uint8

from . import layout, serialize


async def transfer(
    ctx, common: SymbolTransactionCommon, transfer: SymbolTransfer
) -> bytearray:
    await layout.ask_transfer(ctx, common, transfer)
    tx = serialize.serialize_transfer(common, transfer)

    return tx
