from micropython import const

from apps.monero.xmr.serialize.base_types import UVarintType
from apps.monero.xmr.serialize.message_types import ContainerType, MessageType
from apps.monero.xmr.serialize_messages.base import KeyImage

if False:
    from apps.monero.xmr.serialize.base_types import XmrType
    from typing import Tuple, Type


class UVarintTypeContainer(ContainerType):
    ELEM_TYPE = UVarintType


class TxinToKey(MessageType):
    __slots__ = ("amount", "key_offsets", "k_image")
    VARIANT_CODE = const(0x2)

    @classmethod
    def f_specs(cls) -> Tuple[Tuple[str, Type[XmrType]], ...]:
        return (
            ("amount", UVarintType),
            ("key_offsets", UVarintTypeContainer),
            ("k_image", KeyImage),
        )
