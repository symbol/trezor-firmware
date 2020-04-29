if False:
    from typing import Any

import gc


def parse_msg(buf: bytes, msg_type: Any) -> Any:
    from apps.monero.xmr.serialize.readwriter import ByteReader

    reader = ByteReader(memoryview(buf))
    return msg_type.load(reader)


def dump_msg(msg: Any, preallocate: int = 0, prefix: bytes = None) -> bytes:
    from apps.monero.xmr.serialize.readwriter import ByteWriter

    writer = ByteWriter(preallocate)
    if prefix:
        writer.write(prefix)
    msg_type = msg.__class__
    msg_type.dump(writer, msg)

    return writer.get_buffer()


def dump_msg_gc(msg: Any, preallocate: int = 0, prefix: bytes = None) -> bytes:
    buf = dump_msg(msg, preallocate, prefix)
    del msg
    gc.collect()
    return buf
