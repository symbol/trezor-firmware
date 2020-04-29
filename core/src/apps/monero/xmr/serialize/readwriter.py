if False:
    from typing import Union, Protocol, Optional

    class Reader(Protocol):
        def readinto(self, buffer: bytearray) -> Optional[int]:
            pass

    class Writer(Protocol):
        def write(self, buffer: bytes) -> Optional[int]:
            pass


class ByteReader:
    def __init__(self, buffer: Union[bytearray, memoryview]) -> None:
        self.offset = 0
        self.buffer = buffer
        self.buffer_length = len(buffer)

    def readinto(self, buffer: bytearray) -> int:
        buffer_length = len(buffer)
        if buffer_length > 0 and self.offset == self.buffer_length:
            raise EOFError

        read_bytes = min(buffer_length, self.buffer_length - self.offset)

        for i in range(read_bytes):
            buffer[i] = self.buffer[self.offset + i]
        self.offset += read_bytes

        return read_bytes

    async def areadinto(self, buffer: bytearray) -> int:
        return self.readinto(buffer)


def write_to_buffer(
    destination: bytearray, destination_offset: int, source: bytes, source_offset: int
) -> int:
    write_bytes = min(
        len(source) - source_offset, len(destination) - destination_offset
    )
    for i in range(write_bytes):
        destination[destination_offset + i] = source[source_offset + i]
    return write_bytes


class ByteWriter:
    def __init__(self, preallocate: int = 0, allocation_step: int = 32) -> None:
        self.buffer = bytearray(preallocate)
        self.allocation_step = allocation_step
        self.offset = 0

    def write(self, buffer: bytes) -> int:
        buffer_length = len(buffer)

        offset = 0

        written_bytes = write_to_buffer(self.buffer, self.offset, buffer, offset)
        self.offset += written_bytes
        offset += written_bytes

        while offset < buffer_length:
            chunk = bytearray(self.allocation_step)

            written_bytes = write_to_buffer(chunk, 0, buffer, offset)
            self.offset += written_bytes
            offset += written_bytes

            self.buffer.extend(chunk)
        assert offset == buffer_length
        return offset

    async def awrite(self, buffer: bytes) -> int:
        return self.write(buffer)

    def get_buffer(self) -> memoryview:
        return memoryview(self.buffer)[: self.offset]
