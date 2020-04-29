from trezor.utils import HashWriter

from apps.monero.xmr.crypto import get_keccak
from apps.monero.xmr.serialize import int_serialize

if False:
    from trezor.crypto.hashlib import sha3_256


class KeccakXmrArchive:
    def __init__(self, ctx: sha3_256 = None) -> None:
        self.kwriter = get_keccak_writer(ctx)

    def get_digest(self) -> bytes:
        return self.kwriter.get_digest()

    def buffer(self, buf: bytes) -> None:
        self.kwriter.write(buf)

    def uvarint(self, i: int) -> None:
        int_serialize.dump_uvarint(self.kwriter, i)

    def uint(self, i: int, width: int) -> None:
        int_serialize.dump_uint(self.kwriter, i, width)


def get_keccak_writer(ctx: sha3_256 = None) -> HashWriter:
    if ctx is None:
        ctx = get_keccak()
    return HashWriter(ctx)
