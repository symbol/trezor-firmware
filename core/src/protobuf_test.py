from trezorutils import protobuf_decode, protobuf_encode, protobuf_type_for_name
from trezor.utils import BufferReader, BufferWriter
from trezor.enums import Capability
from trezor.enums.Features import Features
from trezor.enums.Ping import Ping
import protobuf
import utime


def dump_message(msg):
    length = protobuf.count_message(msg)
    buffer = bytearray(length)
    protobuf.dump_message(BufferWriter(buffer), msg)
    return buffer


def load_message(buffer, msg_type):
    protobuf.load_message(BufferReader(buffer), msg_type)


def features():
    f = Features(
        vendor="trezor.io",
        language="en-US",
        major_version=0,
        minor_version=0,
        patch_version=0,
        revision=b"000",
        model="test",
        device_id="testtest",
        label="abacbdfa",
        pin_protection=False,
        unlocked=True,
        passphrase_protection=False,
        capabilities=[
            Capability.Bitcoin,
            Capability.Bitcoin_like,
            Capability.Binance,
            Capability.Cardano,
            Capability.Crypto,
            Capability.EOS,
            Capability.Ethereum,
            Capability.Lisk,
            Capability.Monero,
            Capability.NEM,
            Capability.Ripple,
            Capability.Stellar,
            Capability.Tezos,
            Capability.U2F,
            Capability.Shamir,
            Capability.ShamirGroups,
            Capability.PassphraseEntry,
        ],
    )
    return f


def features_new(t):
    f = t(
        vendor="trezor.io",
        language="en-US",
        major_version=0,
        minor_version=0,
        patch_version=0,
        revision=b"000",
        model="test",
        device_id="testtest",
        label="abacbdfa",
        pin_protection=False,
        unlocked=True,
        passphrase_protection=False,
        capabilities=[
            Capability.Bitcoin,
            Capability.Bitcoin_like,
            Capability.Binance,
            Capability.Cardano,
            Capability.Crypto,
            Capability.EOS,
            Capability.Ethereum,
            Capability.Lisk,
            Capability.Monero,
            Capability.NEM,
            Capability.Ripple,
            Capability.Stellar,
            Capability.Tezos,
            Capability.U2F,
            Capability.Shamir,
            Capability.ShamirGroups,
            Capability.PassphraseEntry,
        ],
    )
    return f


def benchmark():
    m = features()
    x = dump_message(m)
    i = 10000

    t = protobuf_type_for_name("Features")
    t0 = utime.ticks_us()
    for _ in range(0, i):
        protobuf_decode(x, t, False)
    t_rust = utime.ticks_diff(utime.ticks_us(), t0)

    t0 = utime.ticks_us()
    for _ in range(0, i):
        load_message(x, Features)
    t_python = utime.ticks_diff(utime.ticks_us(), t0)

    print("rust", t_rust / i, "us/iter")
    print("python", t_python / i, "us/iter")


def codec():
    buf = bytearray(1000)
    t = protobuf_type_for_name("Features")
    m = features_new(t)
    l = protobuf_encode(buf, m)
    n = protobuf_decode(buf[:l], m, False)
    print(m)
    print(n)


def benchmark_new():
    i = 100000

    t = protobuf_type_for_name("Features")
    t0 = utime.ticks_us()
    for _ in range(0, i):
        features_new(t)
    t_rust = utime.ticks_diff(utime.ticks_us(), t0)

    t0 = utime.ticks_us()
    for _ in range(0, i):
        features()
    t_python = utime.ticks_diff(utime.ticks_us(), t0)

    print("rust", t_rust / i, "us/iter")
    print("python", t_python / i, "us/iter")


# codec()
benchmark()
# benchmark_new()
