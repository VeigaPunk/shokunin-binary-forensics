#!/usr/bin/env python3
"""revenger r75 - authored minimal code-bearing PE64 fixture generator.

Builds a 1024-byte PE32+ with one .text section whose entry point is
`mov eax, 0x2a; ret`. Every header field is written explicitly below; the
byte-verify step at the end re-derives the declared premises from the built
bytes (QUALITY.md Q06). Deterministic: no timestamps, no randomness.
Run: python -B gen_pe_r75.py <output.exe>
"""
import struct
import sys

def u16(v): return struct.pack("<H", v)
def u32(v): return struct.pack("<I", v)
def u64(v): return struct.pack("<Q", v)

TOTAL = 1024
buf = bytearray(TOTAL)

# --- DOS header (0x00) ---
buf[0x00:0x02] = b"MZ"
buf[0x3C:0x40] = u32(0x80)          # e_lfanew -> PE signature at 0x80

# --- PE signature (0x80) ---
buf[0x80:0x84] = b"PE\x00\x00"

# --- IMAGE_FILE_HEADER (0x84, 20 bytes) ---
buf[0x84:0x86] = u16(0x8664)        # Machine = AMD64
buf[0x86:0x88] = u16(1)             # NumberOfSections
buf[0x88:0x8C] = u32(0)             # TimeDateStamp = 0 (deterministic)
buf[0x8C:0x90] = u32(0)             # PointerToSymbolTable
buf[0x90:0x94] = u32(0)             # NumberOfSymbols
buf[0x94:0x96] = u16(0xF0)          # SizeOfOptionalHeader (PE32+)
buf[0x96:0x98] = u16(0x0022)        # Characteristics: EXECUTABLE_IMAGE | LARGE_ADDRESS_AWARE

# --- IMAGE_OPTIONAL_HEADER64 (0x98, 112 + 128 = 240 bytes) ---
o = 0x98
buf[o:o+2] = u16(0x020B)            # Magic = PE32+
buf[o+2:o+3] = b"\x00"              # MajorLinkerVersion
buf[o+3:o+4] = b"\x00"              # MinorLinkerVersion
buf[o+4:o+8] = u32(0x200)           # SizeOfCode
buf[o+8:o+12] = u32(0)              # SizeOfInitializedData
buf[o+12:o+16] = u32(0)             # SizeOfUninitializedData
buf[o+16:o+20] = u32(0x1000)        # AddressOfEntryPoint (RVA)
buf[o+20:o+24] = u32(0x1000)        # BaseOfCode
buf[o+24:o+32] = u64(0x140000000)   # ImageBase
buf[o+32:o+36] = u32(0x1000)        # SectionAlignment
buf[o+36:o+40] = u32(0x200)         # FileAlignment
buf[o+40:o+42] = u16(6)             # MajorOperatingSystemVersion
buf[o+42:o+44] = u16(0)             # MinorOperatingSystemVersion
buf[o+44:o+46] = u16(0)             # MajorImageVersion
buf[o+46:o+48] = u16(0)             # MinorImageVersion
buf[o+48:o+50] = u16(6)             # MajorSubsystemVersion
buf[o+50:o+52] = u16(0)             # MinorSubsystemVersion
buf[o+52:o+56] = u32(0)             # Win32VersionValue
buf[o+56:o+60] = u32(0x2000)        # SizeOfImage
buf[o+60:o+64] = u32(0x200)         # SizeOfHeaders
buf[o+64:o+68] = u32(0)             # CheckSum
buf[o+68:o+70] = u16(3)             # Subsystem = IMAGE_SUBSYSTEM_WINDOWS_CUI
buf[o+70:o+72] = u16(0)             # DllCharacteristics
buf[o+72:o+80] = u64(0x100000)      # SizeOfStackReserve
buf[o+80:o+88] = u64(0x1000)        # SizeOfStackCommit
buf[o+88:o+96] = u64(0x100000)      # SizeOfHeapReserve
buf[o+96:o+104] = u64(0x1000)       # SizeOfHeapCommit
buf[o+104:o+108] = u32(0)           # LoaderFlags
buf[o+108:o+112] = u32(16)          # NumberOfRvaAndSizes
# 16 zero DataDirectory entries follow (128 bytes) - already zero.

# --- Section header .text (0x188, 40 bytes) ---
s = 0x188
buf[s:s+8] = b".text\x00\x00\x00"
buf[s+8:s+12] = u32(0x1000)         # VirtualSize
buf[s+12:s+16] = u32(0x1000)        # VirtualAddress
buf[s+16:s+20] = u32(0x200)         # SizeOfRawData
buf[s+20:s+24] = u32(0x200)         # PointerToRawData
buf[s+24:s+28] = u32(0)             # PointerToRelocations
buf[s+28:s+32] = u32(0)             # PointerToLinenumbers
buf[s+32:s+34] = u16(0)             # NumberOfRelocations
buf[s+34:s+36] = u16(0)             # NumberOfLinenumbers
buf[s+36:s+40] = u32(0x60000020)    # Characteristics: CODE|CNT_CODE|MEM_EXECUTE|MEM_READ

# --- Code at file offset 0x200 (RVA 0x1000, entry) ---
# B8 2A 00 00 00   mov eax, 0x2A
# C3               ret
code = bytes.fromhex("B82A000000") + b"\xC3"
buf[0x200:0x200+len(code)] = code

# --- Byte-verify the declared premises against the built bytes (Q06) ---
assert buf[0x00:0x02] == b"MZ"
assert struct.unpack("<I", buf[0x3C:0x40])[0] == 0x80
assert buf[0x80:0x84] == b"PE\x00\x00"
assert struct.unpack("<H", buf[0x84:0x86])[0] == 0x8664
assert struct.unpack("<H", buf[0x86:0x88])[0] == 1
assert struct.unpack("<H", buf[0x94:0x96])[0] == 0xF0
assert struct.unpack("<H", buf[0x98:0x9A])[0] == 0x020B
assert struct.unpack("<I", buf[0xA8:0xAC])[0] == 0x1000, "entry RVA"
assert struct.unpack("<Q", buf[0xB0:0xB8])[0] == 0x140000000, "image base"
assert buf[0x188:0x190] == b".text\x00\x00\x00"
assert struct.unpack("<I", buf[0x194:0x198])[0] == 0x1000, ".text VA"
assert struct.unpack("<I", buf[0x198:0x19C])[0] == 0x200, ".text raw size"
assert struct.unpack("<I", buf[0x19C:0x1A0])[0] == 0x200, ".text raw ptr"
assert buf[0x200:0x205] == bytes.fromhex("B82A000000"), "mov eax,0x2A"
assert buf[0x205:0x206] == b"\xC3", "ret"
assert len(buf) == TOTAL

with open(sys.argv[1], "wb") as fh:
    fh.write(bytes(buf))
print("wrote %s (%d bytes)" % (sys.argv[1], len(buf)))
