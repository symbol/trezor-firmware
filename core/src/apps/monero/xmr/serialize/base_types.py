from apps.monero.xmr.serialize.int_serialize import (
    dump_uint,
    dump_uvarint,
    load_uint,
    load_uvarint,
)

if False:
    from apps.monero.xmr.serialize.readwriter import Reader, Writer
    from typing import Any


class XmrType:
    @staticmethod
    def load(reader: Reader) -> Any:
        pass

    @staticmethod
    def dump(writer: Writer, element: Any) -> None:
        pass


class UVarintType(XmrType):
    @staticmethod
    def load(reader: Reader) -> int:
        return load_uvarint(reader)

    @staticmethod
    def dump(writer: Writer, n: int) -> None:
        dump_uvarint(writer, n)


class IntType(XmrType):
    WIDTH = 0

    @classmethod
    def load(cls, reader: Reader) -> int:
        return load_uint(reader, cls.WIDTH)

    @classmethod
    def dump(cls, writer: Writer, n: int) -> None:
        dump_uint(writer, n, cls.WIDTH)


class UInt8(IntType):
    WIDTH = 1
