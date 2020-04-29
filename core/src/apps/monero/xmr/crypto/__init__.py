# Author: Dusan Klinec, ph4r05, 2018
#
# Resources:
# https://cr.yp.to
# https://github.com/monero-project/mininero
# https://godoc.org/github.com/agl/ed25519/edwards25519
# https://tools.ietf.org/html/draft-josefsson-eddsa-ed25519-00#section-4
# https://github.com/monero-project/research-lab

from trezor.crypto import hmac, monero as tcry, random
from trezor.crypto.hashlib import sha3_256

if False:
    from typing import Tuple, Union
    from apps.monero.xmr.monero import Ge25519, Sc25519

NULL_KEY_ENC = b"\x00" * 32

random_bytes = random.bytes
ct_equals = tcry.ct_equals


def get_keccak(data: bytes = None) -> sha3_256:
    return sha3_256(data=data, keccak=True)


def keccak_hash(data: bytes) -> bytes:
    return tcry.xmr_fast_hash(data)


def keccak_hash_into(output: bytes, data: bytes, length: int = None) -> None:
    if length is None:
        length = len(data)
    tcry.xmr_fast_hash(output, data, length)


def keccak_2hash(data: bytes) -> bytes:
    output = bytearray(32)
    keccak_hash_into(output, data)
    keccak_hash_into(output, output)
    return output


def compute_hmac(key: bytes, msg: bytes) -> bytes:
    h = hmac.new(key, msg=msg, digestmod=get_keccak)
    return h.digest()


#
# EC
#


def new_point() -> Ge25519:
    return tcry.ge25519_set_neutral()


def decodepoint(buff: bytes) -> Ge25519:
    return tcry.ge25519_unpack_vartime(buff)


def decodepoint_into(output: Ge25519, buff: bytes, offset: int = 0) -> None:
    tcry.ge25519_unpack_vartime(output, buff, offset)


def encodepoint(p: Ge25519) -> bytes:
    return tcry.ge25519_pack(p)


def encodepoint_into(
    r: Union[bytearray, memoryview], p: Ge25519, offset: int = 0
) -> None:
    tcry.ge25519_pack(r, p, offset)


def check_ed25519point(r: Ge25519) -> None:
    return tcry.ge25519_check


def decodeint(a: bytes) -> Sc25519:
    return tcry.unpack256_modm(a)


def decodeint_into(r: Sc25519, a: bytes, offset: int = 0) -> None:
    tcry.unpack256_modm(r, a, offset)


def decodeint_noreduce(a: bytes) -> Sc25519:
    return tcry.unpack256_modm_noreduce(a)


def decodeint_noreduce_into(r: Sc25519, a: bytes) -> None:
    tcry.unpack256_modm_noreduce(r, a)


def encodeint(a: Sc25519) -> bytes:
    return tcry.pack256_modm(a)


def encodeint_into(r: bytearray, a: Sc25519, offset: int = 0) -> None:
    tcry.pack256_modm(r, a, offset)


def scalarmult_base(s: Union[Sc25519, int]) -> Ge25519:
    return tcry.ge25519_scalarmult_base(s)


def scalarmult_base_into(r: Ge25519, s: Union[Sc25519, int]) -> None:
    tcry.ge25519_scalarmult_base(r, s)


def scalarmult(p: Ge25519, s: Union[Sc25519, int]) -> Ge25519:
    return tcry.ge25519_scalarmult(p, s)


def scalarmult_into(r: Ge25519, p: Ge25519, s: Union[Sc25519, int]) -> None:
    tcry.ge25519_scalarmult(r, p, s)


def point_add(a: Ge25519, b: Ge25519) -> Ge25519:
    return tcry.ge25519_add(a, b)


def point_add_into(r: Ge25519, a: Ge25519, b: Ge25519) -> None:
    tcry.ge25519_add(r, a, b)


def point_sub(a: Ge25519, b: Ge25519) -> Ge25519:
    return tcry.ge25519_sub(a, b)


def point_sub_into(r: Ge25519, a: Ge25519, b: Ge25519) -> None:
    tcry.ge25519_sub(r, a, b)


def point_eq(a: Ge25519, b: Ge25519) -> bool:
    return tcry.ge25519_eq(a, b)


def point_double(p: Ge25519) -> Ge25519:
    return tcry.ge25519_double(p)


def point_double_into(r: Ge25519, p: Ge25519) -> None:
    tcry.ge25519_double(r, p)


def point_mul8(p: Ge25519) -> Ge25519:
    return tcry.ge25519_mul8(p)


def point_mul8_into(r: Ge25519, p: Ge25519) -> None:
    tcry.ge25519_mul8(r, p)


INV_EIGHT = b"\x79\x2f\xdc\xe2\x29\xe5\x06\x61\xd0\xda\x1c\x7d\xb3\x9d\xd3\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06"
INV_EIGHT_SC = decodeint(INV_EIGHT)


def new_scalar() -> Sc25519:
    return tcry.init256_modm()


def sc_inv_eight() -> Sc25519:
    return INV_EIGHT_SC


#
# Zmod(order), scalar values field
#


def sc_0() -> Sc25519:
    return tcry.init256_modm(0)


def sc_0_into(r: Sc25519) -> Sc25519:
    return tcry.init256_modm(r, 0)


def sc_init(x: int) -> Sc25519:
    if x >= (1 << 64):
        raise ValueError("Initialization works up to 64-bit only")
    return tcry.init256_modm(x)


def sc_init_into(r: Sc25519, x: int) -> Sc25519:
    if x >= (1 << 64):
        raise ValueError("Initialization works up to 64-bit only")
    return tcry.init256_modm(r, x)


def sc_copy(dst: Sc25519, val: Sc25519):
    tcry.init256_modm(dst, val)


def sc_get64(a: Sc25519) -> int:
    return tcry.get256_modm(a)


def sc_check(val: Sc25519) -> None:
    return tcry.check256_modm


def sc_add(a: Sc25519, b: Sc25519) -> Sc25519:
    return tcry.add256_modm(a, b)


def sc_add_into(r: Sc25519, a: Sc25519, b: Sc25519) -> None:
    tcry.add256_modm(r, a, b)


def sc_sub(a: Sc25519, b: Sc25519) -> Sc25519:
    return tcry.sub256_modm(a, b)


def sc_sub_into(r: Sc25519, a: Sc25519, b: Sc25519) -> None:
    tcry.sub256_modm(r, a, b)


def sc_mul(a: Sc25519, b: Sc25519) -> Sc25519:
    return tcry.mul256_modm(a, b)


def sc_mul_into(r: Sc25519, a: Sc25519, b: Sc25519) -> None:
    tcry.mul256_modm(r, a, b)


def sc_isnonzero(c: Sc25519) -> bool:
    """
    Returns true if scalar is non-zero
    """
    return not tcry.iszero256_modm(c)


def sc_eq(a: Sc25519, b: Sc25519) -> bool:
    return tcry.eq256_modm(a, b) == 1


def sc_mulsub(a: Sc25519, b: Sc25519, c: Sc25519) -> Sc25519:
    return tcry.mulsub256_modm(a, b, c)


def sc_mulsub_into(r: Sc25519, a: Sc25519, b: Sc25519, c: Sc25519) -> None:
    tcry.mulsub256_modm(r, a, b, c)


def sc_muladd(a: Sc25519, b: Sc25519, c: Sc25519) -> Sc25519:
    return tcry.muladd256_modm(a, b, c)


def sc_muladd_into(r: Sc25519, a: Sc25519, b: Sc25519, c: Sc25519) -> None:
    tcry.muladd256_modm(r, a, b, c)


def sc_inv_into(r: Sc25519, a: Sc25519) -> None:
    tcry.inv256_modm(r, a)


def sc_inv(r: Sc25519, a: Sc25519) -> Sc25519:
    return tcry.inv256_modm(a)


def random_scalar() -> Sc25519:
    return tcry.xmr_random_scalar()


def random_scalar_into(r: Sc25519) -> None:
    return tcry.xmr_random_scalar(r)


#
# GE - ed25519 group
#


def ge25519_double_scalarmult_base_vartime(
    a: Sc25519, A: Ge25519, b: Sc25519
) -> Ge25519:
    """
    void ge25519_double_scalarmult_vartime(ge25519 *r, const ge25519 *p1, const bignum256modm s1, const bignum256modm s2);
    r = a * A + b * B
    """
    R = tcry.ge25519_double_scalarmult_vartime(A, a, b)
    return R


ge25519_double_scalarmult_vartime2 = tcry.xmr_add_keys3


def identity(byte_enc: bool = False) -> Union[Ge25519, bytes]:
    idd = tcry.ge25519_set_neutral(None)
    return idd if not byte_enc else encodepoint(idd)


def identity_into(r: Ge25519) -> None:
    tcry.ge25519_set_neutral(r)


"""
https://www.imperialviolet.org/2013/12/25/elligator.html
http://elligator.cr.yp.to/
http://elligator.cr.yp.to/elligator-20130828.pdf
"""

#
# Monero specific
#


cn_fast_hash = keccak_hash


def hash_to_scalar(data: bytes) -> Sc25519:
    """
    H_s(P)
    """
    return tcry.xmr_hash_to_scalar(data)


def hash_to_scalar_into(r: Sc25519, data: bytes) -> Sc25519:
    return tcry.xmr_hash_to_scalar(r, data)


"""
H_p(buf)

Code adapted from MiniNero: https://github.com/monero-project/mininero
https://github.com/monero-project/research-lab/blob/master/whitepaper/ge_fromfe_writeup/ge_fromfe.pdf
http://archive.is/yfINb
"""


def hash_to_point(buff: bytes) -> Ge25519:
    return tcry.xmr_hash_to_ec(buff)


def hash_to_point_into(r: Ge25519, buff: bytes) -> None:
    tcry.xmr_hash_to_ec(r, buff)


#
# XMR
#


def xmr_H() -> Ge25519:
    return tcry.ge25519_set_xmr_h(None)


def scalarmult_h(i: Union[int, Sc25519]) -> Ge25519:
    return scalarmult(xmr_H(), sc_init(i) if isinstance(i, int) else i)


def add_keys2(a: Sc25519, b: Sc25519, B: Ge25519) -> Ge25519:
    return tcry.xmr_add_keys2_vartime(a, b, B)


def add_keys2_into(r: Ge25519, a: Sc25519, b: Sc25519, B: Ge25519) -> None:
    tcry.xmr_add_keys2_vartime(r, a, b, B)


def add_keys3(r: Ge25519, a: Sc25519, A: Ge25519, b: Sc25519, B: Ge25519) -> Ge25519:
    return tcry.xmr_add_keys3_vartime(a, A, b, B)


def add_keys3_into(r: Ge25519, a: Sc25519, A: Ge25519, b: Sc25519, B: Ge25519) -> None:
    tcry.xmr_add_keys3_vartime(r, a, A, b, B)


def gen_commitment(a: Sc25519, amount: int) -> Ge25519:
    return tcry.xmr_gen_c(a, amount)


def generate_key_derivation(pub: Ge25519, sec: Sc25519) -> Ge25519:
    """
    Key derivation: 8*(key2*key1)
    """
    sc_check(sec)  # checks that the secret key is uniform enough...
    check_ed25519point(pub)
    return tcry.xmr_generate_key_derivation(pub, sec)


def derivation_to_scalar(derivation: Ge25519, output_index: int) -> Sc25519:
    """
    H_s(derivation || varint(output_index))
    """
    check_ed25519point(derivation)
    return tcry.xmr_derivation_to_scalar(derivation, output_index)


def derive_public_key(derivation: Ge25519, output_index: int, B: Ge25519) -> Ge25519:
    """
    H_s(derivation || varint(output_index))G + B
    """
    check_ed25519point(B)
    return tcry.xmr_derive_public_key(derivation, output_index, B)


def derive_secret_key(derivation: Ge25519, output_index: int, base: Sc25519) -> Sc25519:
    """
    base + H_s(derivation || varint(output_index))
    """
    sc_check(base)
    return tcry.xmr_derive_private_key(derivation, output_index, base)


def get_subaddress_secret_key(
    secret_key: Sc25519, major: int = 0, minor: int = 0
) -> Sc25519:
    """
    Builds subaddress secret key from the subaddress index
    Hs(SubAddr || a || index_major || index_minor)
    """
    return tcry.xmr_get_subaddress_secret_key(major, minor, secret_key)


def generate_signature(data: bytes, priv: Sc25519) -> Tuple[Sc25519, Sc25519, Ge25519]:
    """
    Generate EC signature
    crypto_ops::generate_signature(const hash &prefix_hash, const public_key &pub, const secret_key &sec, signature &sig)
    """
    pub = scalarmult_base(priv)

    k = random_scalar()
    comm = scalarmult_base(k)

    buff = data + encodepoint(pub) + encodepoint(comm)
    c = hash_to_scalar(buff)
    r = sc_mulsub(priv, c, k)
    return c, r, pub


def check_signature(data: bytes, c: Sc25519, r: Sc25519, pub: Ge25519) -> bool:
    """
    EC signature verification
    """
    check_ed25519point(pub)
    if sc_check(c) != 0 or sc_check(r) != 0:
        raise ValueError("Signature error")

    tmp2 = point_add(scalarmult(pub, c), scalarmult_base(r))
    buff = data + encodepoint(pub) + encodepoint(tmp2)
    tmp_c = hash_to_scalar(buff)
    res = sc_sub(tmp_c, c)
    return not sc_isnonzero(res)


def xor8(buff: bytearray, key: bytes) -> bytes:
    for i in range(8):
        buff[i] ^= key[i]
    return buff
