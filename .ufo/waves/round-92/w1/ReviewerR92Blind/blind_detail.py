#!/usr/bin/env python3
"""Blind detail pass, reviewer's own code: IL body, signature blob, #US literal.

Chains off the reviewer's own first-pass offsets (blind_parse.py output), never
the lane's scripts or records. Reads only fixture bytes.
"""
import hashlib
import struct
import sys

path = sys.argv[1]
data = open(path, "rb").read()

# constants from my own first pass (blind_parse_output.txt):
TEXT_VA, TEXT_RAW = 0x1000, 0x200
MD_ROOT = 0x280           # metadata root file offset
BLOB_HEAP = MD_ROOT + 0x184   # #Blob stream offset from root
US_HEAP = MD_ROOT + 0x154     # #US stream offset from root
METHODDEF_TABLE = 0x342       # my derived MethodDef row 1 file offset
ROW_SIZE = 14                 # RVA4 ImplFlags2 Flags2 Name2 Sig2 ParamList2

def rva2off(rva):
    assert TEXT_VA <= rva < TEXT_VA + 0x10000
    return rva - TEXT_VA + TEXT_RAW

print(f"detail pass over {path}")

# --- m0 body: tiny format
body_rva = struct.unpack_from("<I", data, METHODDEF_TABLE)[0]
body_off = rva2off(body_rva)
first = data[body_off]
assert first & 0x3 == 2, f"not a tiny header: {first:#x}"
il_size = first >> 2
il = data[body_off + 1: body_off + 1 + il_size]
print(f"m0.body: rva=0x{body_rva:x} file_offset={body_off} format=tiny il_size={il_size}")
print(f"m0.body.il_bytes: {il.hex()}")
print(f"m0.body.il_sha256: {hashlib.sha256(il).hexdigest()}")
# opcodes of interest
ops = []
i = 0
while i < len(il):
    b = il[i]
    if b == 0x72:
        tok = struct.unpack_from("<I", il, i + 1)[0]
        ops.append((i, "ldstr", f"0x{tok:08x}"))
        i += 5
    elif b == 0x2A:
        ops.append((i, "ret", None))
        i += 1
    else:
        ops.append((i, f"opcode_0x{b:02x}", None))
        i += 1
print(f"m0.body.ops: {ops}")

# --- m0 signature blob
sig_idx = struct.unpack_from("<H", data, METHODDEF_TABLE + 10)[0]
blob_off = BLOB_HEAP + sig_idx
lb = data[blob_off]
if lb & 0x80 == 0:
    sig_len = lb
    raw = data[blob_off + 1: blob_off + 1 + sig_len]
elif lb & 0xC0 == 0x80:
    sig_len = ((lb & 0x3F) << 8) | data[blob_off + 1]
    raw = data[blob_off + 2: blob_off + 2 + sig_len]
else:
    raise SystemExit("4-byte blob length not handled")
conv = raw[0] & 0x0F
params = raw[1]
ret = raw[2]
RET = {0x0E: "string", 0x01: "void", 0x08: "int32", 0x0C: "object"}
print(f"m0.sig: blob_index={sig_idx} heap_file_offset={blob_off} raw_length={sig_len}")
print(f"m0.sig.raw_bytes: {raw.hex()}")
print(f"m0.sig.raw_sha256: {hashlib.sha256(raw).hexdigest()}")
print(f"m0.sig.decode: conv={'default' if conv == 0 else hex(conv)} params={params} return={RET.get(ret, hex(ret))}")

# --- #US literal for token 0x70000001
us_off = US_HEAP + 1  # heap offset 0 holds one 0x00 byte; token 0x70000001 -> heap offset 1
print(f"#US heap file offset: {US_HEAP} (heap byte 0 = {data[US_HEAP]:#04x})")
lb = data[us_off]
if lb & 0x80 == 0:
    n = lb
    payload = data[us_off + 1: us_off + 1 + n]
elif lb & 0xC0 == 0x80:
    n = ((lb & 0x3F) << 8) | data[us_off + 1]
    payload = data[us_off + 2: us_off + 2 + n]
else:
    raise SystemExit("4-byte US length not handled")
s = payload[:-1].decode("utf-16-le")  # last byte = flag
print(f"us.lit: heap_offset={us_off} compressed_len_bytes={n} value={s!r} flag_byte={payload[-1]:#04x}")
