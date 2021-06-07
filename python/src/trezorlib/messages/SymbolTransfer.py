# Automatically generated by pb2py
# fmt: off
# isort:skip_file
from .. import protobuf as p

from .SymbolMosaic import SymbolMosaic

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class SymbolTransfer(p.MessageType):

    def __init__(
        self,
        *,
        mosaics: Optional[List[SymbolMosaic]] = None,
        recipient_address: Optional[str] = None,
        message: Optional[bytes] = None,
    ) -> None:
        self.mosaics = mosaics if mosaics is not None else []
        self.recipient_address = recipient_address
        self.message = message

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('recipient_address', p.UnicodeType, None),
            2: ('mosaics', SymbolMosaic, p.FLAG_REPEATED),
            3: ('message', p.BytesType, None),
        }
