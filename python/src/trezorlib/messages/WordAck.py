# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class WordAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 47

    def __init__(
        self,
        word: str = None,
    ) -> None:
        self.word = word

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('word', p.UnicodeType, 0),  # required
        }