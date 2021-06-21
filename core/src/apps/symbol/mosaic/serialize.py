from apps.common.writers import write_bytes_unchecked, write_uint32_le, write_uint64_le, write_uint8, write_uint16_le
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolMosaicDefinition  import SymbolMosaicDefinition
from trezor.messages.SymbolMosaicSupplyChange import SymbolMosaicSupplyChange
from trezor.messages import SymbolEntityType

from ..common_serializors import serialize_tx_header


def serialize_mosaic_definition(
    header: SymbolHeader, definition: SymbolMosaicDefinition
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.MOSAIC_DEFINITION)

    write_uint64_le( tx, definition.id )
    write_uint64_le( tx, definition.duration )
    write_uint32_le( tx, definition.nonce )
    write_uint8( tx, definition.flags )
    write_uint8( tx, definition.divisibility )

    return tx

def serialize_mosaic_supply_change(
    header: SymbolHeader, supply: SymbolMosaicSupplyChange
) -> bytearray:
    tx = serialize_tx_header(header, SymbolEntityType.MOSAIC_SUPPLY_CHANGE)

    write_uint64_le( tx, supply.mosaic.id )
    write_uint64_le( tx, supply.mosaic.amount )
    write_uint8( tx, supply.action )

    return tx
