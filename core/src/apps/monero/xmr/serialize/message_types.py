from trezor.utils import obj_eq, obj_repr

from apps.monero.xmr.serialize.base_types import XmrType
from apps.monero.xmr.serialize.int_serialize import (
    dump_uint,
    dump_uvarint,
    load_uint,
    load_uvarint,
)

if False:
    from typing import List, Tuple, Any, Type
    from apps.monero.xmr.serialize.readwriter import Reader, Writer


class UnicodeType(XmrType):
    """
    Unicode data in UTF-8 encoding.
    """

    @staticmethod
    def dump(writer: Writer, s: str) -> None:
        dump_uvarint(writer, len(s))
        writer.write(bytes(s, encoding="utf8"))

    @staticmethod
    def load(reader: Reader) -> str:
        ivalue = load_uvarint(reader)
        fvalue = bytearray(ivalue)
        reader.readinto(fvalue)
        return str(fvalue)


class BlobType(XmrType):
    """
    Binary data, represented as bytearray.  BlobType is only a scheme
    descriptor.  Behaves in the same way as primitive types.
    """

    FIX_SIZE = 0
    SIZE = 0

    @classmethod
    def dump(cls, writer: Writer, elem: bytes) -> None:
        if cls.FIX_SIZE:
            if cls.SIZE != len(elem):
                raise ValueError("Size mismatch")
        else:
            dump_uvarint(writer, len(elem))
        writer.write(elem)

    @classmethod
    def load(cls, reader: Reader) -> bytearray:
        if cls.FIX_SIZE:
            size = cls.SIZE
        else:
            size = load_uvarint(reader)
        elem = bytearray(size)
        reader.readinto(elem)
        return elem


class ContainerType(XmrType):
    """
    Array of elements, represented as a list of items.  ContainerType is only a
    scheme descriptor.
    """

    FIX_SIZE = 0
    SIZE = 0
    ELEM_TYPE = None  # type: Type[XmrType]

    @classmethod
    def dump(cls, writer: Writer, elems: List[XmrType]) -> None:
        assert cls.ELEM_TYPE is not None
        if cls.FIX_SIZE:
            if cls.SIZE != len(elems):
                raise ValueError("Size mismatch")
        else:
            dump_uvarint(writer, len(elems))
        for elem in elems:
            cls.ELEM_TYPE.dump(writer, elem)

    @classmethod
    def load(cls, reader: Reader) -> List[XmrType]:
        assert cls.ELEM_TYPE is not None
        if cls.FIX_SIZE:
            size = cls.SIZE
        else:
            size = load_uvarint(reader)
        elems = []
        for _ in range(size):
            elem = cls.ELEM_TYPE.load(reader)
            elems.append(elem)
        return elems


class VariantType(XmrType):
    """
    Union of types, differentiated by variant tags. VariantType is only a scheme
    descriptor.
    """

    @classmethod
    def dump(cls, writer: Writer, elem: "VariantType") -> None:
        for field in cls.f_specs():
            fcode, ftype = field
            if isinstance(elem, ftype):
                dump_uint(writer, fcode, 1)
                ftype.dump(writer, elem)
                break
        else:
            raise ValueError("Unrecognized variant: %s" % elem)

    @classmethod
    def load(cls, reader: Reader) -> Any:
        tag = load_uint(reader, 1)
        for field in cls.f_specs():
            fcode, ftype = field
            if fcode == tag:
                fvalue = ftype.load(reader)
                break
        else:
            raise ValueError("Unknown tag: %s" % tag)
        return fvalue

    @classmethod
    def f_specs(cls) -> Tuple[Tuple[int, Type[XmrType]], ...]:
        return ()


class MessageType(XmrType):
    """
    Message composed of fields with specific types.
    """

    def __init__(self, **kwargs: Any) -> None:
        for kw in kwargs:
            setattr(self, kw, kwargs[kw])

    __eq__ = obj_eq
    __repr__ = obj_repr

    @classmethod
    def dump(cls, writer: Writer, msg: "MessageType") -> None:
        defs = cls.f_specs()
        for field in defs:
            fname, ftype = field
            fvalue = getattr(msg, fname, None)
            ftype.dump(writer, fvalue)

    @classmethod
    def load(cls, reader: Reader) -> "MessageType":
        msg = cls()
        defs = cls.f_specs()
        for field in defs:
            fname, ftype = field
            fvalue = ftype.load(reader)
            setattr(msg, fname, fvalue)
        return msg

    @classmethod
    def f_specs(cls) -> Tuple[Tuple[str, Type[XmrType]], ...]:
        return ()
