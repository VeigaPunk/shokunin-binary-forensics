#!/usr/bin/env python
"""gen_native_auth_r79.py - build a minimal native PE32 fixture carrying one
WIN_CERTIFICATE table entry (PKCS#7 signedData, structural only).

Authored for round-79 claim C1: a real `rea inspect-pe-certificates` producer
record on an in-province surface the frozen F mapping did not cover. The
generator derives every header field from the built bytes (Q06: premises
re-derived from the built image, not from intent) and refuses to write unless
all asserts pass. Deterministic: same inputs -> byte-identical image.

The embedded PKCS#7 blob is structurally valid DER (ContentInfo -> signedData
with one SignerInfo) and cryptographically meaningless by construction: the
producer's own limitations say it decodes structure and never verifies
signatures, chains or digests. Nothing here is a real credential.
"""
import hashlib
import struct
import sys
from pathlib import Path

SECTION_ALIGN = 0x1000
FILE_ALIGN = 0x200
IMAGE_BASE = 0x400000

SECTION_MARK = b"R79AUTHENTICODEPROBE"     # authored .text fill
CERT_REVISION = 0x0200                     # WIN_CERT_REVISION_2_0
CERT_TYPE_PKCS7 = 0x0002                   # WIN_CERT_TYPE_PKCS_SIGNED_DATA
SKI_BYTES = bytes([0xAB, 0xCD])            # SignerIdentifier subjectKeyIdentifier
SIGNATURE_BYTES = bytes(16)                # structurally present, no meaning


def _tlv(tag: int, body: bytes) -> bytes:
    if len(body) < 0x80:
        return bytes([tag, len(body)]) + body
    lb = len(body).to_bytes((len(body).bit_length() + 7) // 8, "big")
    return bytes([tag, 0x80 | len(lb)]) + lb + body


def build_payload() -> bytes:
    """Minimal DER PKCS#7 ContentInfo (signedData, one SignerInfo)."""
    oid_signed = bytes([0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x07, 0x02])
    oid_data = bytes([0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x07, 0x01])
    oid_sha256 = bytes([0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01])
    oid_rsa = bytes([0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x01, 0x01])
    version = _tlv(0x02, b"\x01")
    sid = _tlv(0x80, SKI_BYTES)                       # [0] IMPLICIT OCTET STRING
    digest_alg = _tlv(0x30, _tlv(0x06, oid_sha256) + _tlv(0x05, b""))
    sig_alg = _tlv(0x30, _tlv(0x06, oid_rsa) + _tlv(0x05, b""))
    signature = _tlv(0x04, SIGNATURE_BYTES)
    signer = _tlv(0x30, version + sid + digest_alg + sig_alg + signature)
    signer_infos = _tlv(0x31, signer)
    digest_algs = _tlv(0x31, _tlv(0x30, _tlv(0x06, oid_sha256) + _tlv(0x05, b"")))
    encap = _tlv(0x30, _tlv(0x06, oid_data))
    signed_data = _tlv(0x30, version + digest_algs + encap + signer_infos)
    content = _tlv(0xA0, signed_data)
    return _tlv(0x30, _tlv(0x06, oid_signed) + content)


def build(cert_payload: bytes) -> bytes:
    text = SECTION_MARK.ljust(0x40, b"\x00")
    assert len(text) == 0x40

    dos = bytearray(b"\x00" * 0x40)
    dos[0:2] = b"MZ"
    struct.pack_into("<I", dos, 0x3C, 0x40)
    pe = bytearray()
    pe += b"PE\x00\x00"
    pe += struct.pack("<HHIIIHH", 0x014C, 1, 0, 0, 0, 0xE0, 0x2102)
    opt = bytearray()
    opt += struct.pack("<HBB", 0x10B, 8, 0)
    opt += struct.pack("<III", 0x40, 0, 0)
    opt += struct.pack("<III", 0, 0x1000, 0)
    opt += struct.pack("<III", IMAGE_BASE, SECTION_ALIGN, FILE_ALIGN)
    opt += struct.pack("<HHHHHH", 4, 0, 1, 0, 4, 0)
    opt += struct.pack("<I", 0)
    opt += struct.pack("<I", SECTION_ALIGN)          # SizeOfImage
    opt += struct.pack("<I", FILE_ALIGN)             # SizeOfHeaders
    opt += struct.pack("<I", 0)                      # CheckSum
    opt += struct.pack("<HH", 3, 0)
    opt += struct.pack("<II", 0x100000, 0x1000)
    opt += struct.pack("<II", 0x100000, 0x1000)
    opt += struct.pack("<II", 0, 16)
    ddirs = [(0, 0)] * 16                            # ddir[4] patched below
    for va, sz in ddirs:
        opt += struct.pack("<II", va, sz)
    assert len(opt) == 0xE0, hex(len(opt))

    sect = struct.pack("<8sIIIIIIHHI", b".text", 0x1000, 0x1000, FILE_ALIGN,
                       FILE_ALIGN, 0, 0, 0, 0, 0x60000020)

    image = bytearray()
    image += dos
    image += pe
    image += opt
    image += sect
    image += b"\x00" * (FILE_ALIGN - len(image))
    image += text
    image += b"\x00" * (FILE_ALIGN - len(text))

    # certificate table: file offset (the security directory is file-based),
    # 8-aligned; dwLength equals the declared table size exactly (8-aligned
    # per the WIN_CERTIFICATE alignment rule).
    cert_off = (len(image) + 7) & ~7
    image += b"\x00" * (cert_off - len(image))
    padded = cert_payload + b"\x00" * ((-len(cert_payload)) % 8)
    dw_len = 8 + len(padded)
    image += struct.pack("<IHH", dw_len, CERT_REVISION, CERT_TYPE_PKCS7)
    image += padded
    table_size = len(image) - cert_off
    assert table_size == dw_len, (table_size, dw_len)

    ddir4_off = 0x40 + 4 + 20 + 0x60 + 4 * 8
    struct.pack_into("<II", image, ddir4_off, cert_off, table_size)
    return bytes(image)


def self_check(image: bytes, cert_payload: bytes) -> dict:
    """Re-derive every declared premise from the built bytes (Q06)."""
    assert image[:2] == b"MZ"
    e_lfanew, = struct.unpack_from("<I", image, 0x3C)
    assert e_lfanew == 0x40
    assert image[e_lfanew:e_lfanew + 4] == b"PE\x00\x00"
    machine, nsec, _, _, _, opt_size, chars = struct.unpack_from(
        "<HHIIIHH", image, e_lfanew + 4)
    assert machine == 0x014C and nsec == 1 and opt_size == 0xE0
    ddir = e_lfanew + 24 + 0x60
    num_dd, = struct.unpack_from("<I", image, e_lfanew + 24 + 0x5C)
    assert num_dd == 16
    cert_off, cert_size = struct.unpack_from("<II", image, ddir + 4 * 8)
    assert cert_off > 0 and cert_size > 0
    assert cert_off % 8 == 0
    dw_len, rev, ctype = struct.unpack_from("<IHH", image, cert_off)
    assert dw_len == cert_size, (dw_len, cert_size)
    assert (rev, ctype) == (CERT_REVISION, CERT_TYPE_PKCS7)
    payload_off = cert_off + 8
    payload_len = dw_len - 8
    assert image[payload_off:payload_off + len(cert_payload)] == cert_payload
    assert image[payload_off + len(cert_payload):payload_off + payload_len] \
        == b"\x00" * (payload_len - len(cert_payload))
    sec_off = e_lfanew + 24 + opt_size
    name, vsize, va, rsize, praw = struct.unpack_from("<8sIIII", image, sec_off)
    assert name.rstrip(b"\x00") == b".text" and va == 0x1000 and praw == FILE_ALIGN
    mark = image[praw:praw + len(SECTION_MARK)]
    assert mark == SECTION_MARK
    return {
        "table_offset": cert_off,
        "table_bytes": cert_size,
        "entry_length": dw_len,
        "revision": rev,
        "cert_type": ctype,
        "payload_offset": payload_off,
        "payload_bytes": len(cert_payload),
        "payload_sha256": hashlib.sha256(cert_payload).hexdigest(),
        "image_sha256": hashlib.sha256(image).hexdigest(),
        "image_bytes": len(image),
        "ddir4_offset": ddir + 4 * 8,
    }


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("fixture.dll")
    payload = build_payload()
    image = build(payload)
    facts = self_check(image, payload)
    out.write_bytes(image)
    print("self-check OK: native PE32 certificate-table premises re-derived "
          "from built bytes")
    for k in sorted(facts):
        print(f"{k}={facts[k]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
