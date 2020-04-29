if False:
    from apps.monero.xmr.crypto import Sc25519


class CtKey:
    __slots__ = ("dest", "mask")

    def __init__(self, dest: Sc25519, mask: Sc25519):
        self.dest = dest
        self.mask = mask
