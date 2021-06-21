from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolTransfer import SymbolTransfer


from apps.common.writers import write_bytes_unchecked, write_uint16_le, write_uint32_le, write_uint64_le, write_uint8

from . import layout, serialize


async def transfer(
    ctx, header: SymbolHeader, transfer: SymbolTransfer
) -> bytearray:
    await layout.ask_transfer(ctx, header, transfer)
    tx = serialize.serialize_transfer(header, transfer)

    return tx
