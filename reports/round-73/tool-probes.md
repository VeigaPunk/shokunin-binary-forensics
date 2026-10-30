# Round 73: RE toolbench installs and probes

Date: 2026-10-29. Host: Arch Linux x64 (kernel 7.2.11-arch1-1). Agent: `REVENGER_SHOKUNIN.ReToolbenchInstaller`.

Rules followed: no `pacman -Sy` or `-Syu`; every package was checked with `pacman -Si` before install; no AUR. Probes ran only against system binaries (`/usr/bin/true`, `/bin/true`, `/usr/bin/false`, the SDK's own `dotnet.dll`) or tiny fixtures written in a temp dir (YARA rule, `.wat`, `.ksy`). No sample binaries were executed. No repo files other than this report were touched.

## Installs

| tool | version | channel | reason |
|---|---|---|---|
| ghidra | 12.1.2-2 | pacman (extra) | decompiler / headless analysis |
| yara | 4.5.8-1 | pacman (extra) | signature scanning |
| python-pefile | 2024.8.26-2 | pacman (extra) | PE parsing |
| capstone + python-capstone | 5.0.9-1 (py module reports 5.0.7) | pacman (extra) | disassembly library / `cstool` |
| keystone + python-keystone | 0.9.2-9 | pacman (extra) | assembler library / `kstool` |
| unicorn + python-unicorn | 2.1.4-2 | pacman (extra) | CPU emulation |
| pwndbg | 2026.09.15-1 | pacman (extra) | gdb RE/exploit plugin |
| gef | 2026.01-1 | pacman (extra) | alternative gdb plugin (`/usr/share/gef/gef.py`) |
| diffoscope | 331-1 | pacman (extra) | deep binary/artifact diffing |
| checksec | 3.2.0-2 | pacman (extra) | ELF hardening flags |
| rz-cutter | 2.4.1-8 | pacman (extra) | Rizin GUI (note: pacman `cutter` 1.04 is an unrelated TCP tool, not installed) |
| wabt | 1.0.42-1 | pacman (extra) | wasm tools (wat2wasm, wasm-objdump, …) |
| ltrace | 0.8.1-1 | pacman (extra) | library-call tracing |
| binaryen | 1:130-1 | pacman (extra) | wasm-opt / wasm-dis |
| patchelf | 0.19.2-1 | pacman (extra) | ELF interpreter/needed inspection |
| dotnet-sdk (+ deps, incl. dotnet-targeting-pack) | 10.0.13.sdk113-1 | pacman (extra) | needed to run ilspycmd |
| flare-capa | 10.0.0 | `uv tool install --python 3.12` | capability detection (3.14 install failed: `python-flirt` build error) |
| capa-rules | v10.0.0 (tarball, sha256 below) | official GitHub tag tarball → `~/.local/share/capa-rules` | the uv-installed capa has no embedded rules; pass `-r ~/.local/share/capa-rules` |
| flare-floss | 3.2.0 | `uv tool install --python 3.12` | obfuscated string extraction (same python-flirt reason) |
| pyinstxtractor-ng | (PyPI latest, xdis 6.3.0) | `uv tool install` | PyInstaller archive extraction |
| lief | 1.0.0 | `uv venv ~/.local/share/re-pyenv` + `uv pip install lief` | not in pacman; library only, no CLI, so it gets a dedicated venv (`~/.local/share/re-pyenv/bin/python`) |
| ilspycmd | 11.2.0.10050 | `dotnet tool install -g` (`~/.dotnet/tools`) | .NET decompiler CLI |
| detect-it-easy (die/diec/diel) | 3.21 | official GitHub release `detect-it-easy-3.21-1-x86_64.pkg.tar.zst` via `pacman -U` (sha256 below) | file type, compiler and packer ID; not in official repos |
| imhex (imhex-bin, pulled mbedtls) | 1.38.1 | official GitHub release `imhex-1.38.1-ArchLinux-x86_64.pkg.tar.zst` via `pacman -U` (sha256 below) | pattern-language hex editor; not in official repos |
| kaitai-struct-compiler | 0.11 | official GitHub release zip → `~/.local/opt/`, symlink in `~/.local/bin` (sha256 below) | .ksy format compiler; uses the system JDK 21 |
| apktool | 3.0.3 | official GitHub release jar → `~/.local/opt/apktool/`, wrapper `~/.local/bin/apktool` (sha256 below) | APK decode |
| rr | 5.10.0 | official GitHub release tarball → `~/.local/opt/`, symlink in `~/.local/bin` (sha256 below) | record/replay debugging; not in pacman repos |

The full checksums of the downloaded assets are in `~/tmp/re-dl/` (computed with `sha256sum` at download time):
`apktool_3.0.3.jar dbf930b076c6b9be08d57c449cacefc3bdd6b71ebd59b3066fc0e1f5b14f9423`,
`detect-it-easy-3.21-1-x86_64.pkg.tar.zst 7fb930ae53f80f50720c54f0d7a4c9c1a624ba084baa2b43a040f338565e13e1`,
`imhex-1.38.1-ArchLinux-x86_64.pkg.tar.zst c667f5d7ce9754f9a90338967a3c6077c256d4a4acd25e76fb3027ba4290d39e`,
`kaitai-struct-compiler-0.11.zip ff89389d9dc9e770d78a24af328763cb1f8e7b31ce7766c9edf10669a060f2a2`,
`rr-5.10.0-Linux-x86_64.tar.gz 55d9175d88139f775aca36981c55c2f3bca227434217750fc3ee2619501e269b`,
`capa-rules-v10.0.0.tar.gz d0f4e88098d7571e5c5f47f7320cff0786d48c81512806952ac2d396c1a0ed86`.

## Probes

PATH included `~/.local/bin` and `~/.dotnet/tools`. Cutter and ImHex ran with `QT_QPA_PLATFORM=offscreen`. `$T` is the temp fixture dir.

| tool | command | exit | observed output (first line / key line) | date |
|---|---|---|---|---|
| ghidra | `grep '^application.version' /opt/ghidra/Ghidra/application.properties` | 0 | `application.version=12.1.2` | 2026-10-29 |
| ghidra | `ghidra-analyzeHeadless $T gproj2 -import /usr/bin/true -deleteProject -noanalysis` | 0 | `INFO  REPORT: Import succeeded (HeadlessAnalyzer)` | 2026-10-29 |
| capa | `capa --version` | 0 | `capa 10.0.0` | 2026-10-29 |
| capa | `capa -q -j /usr/bin/true` (no rules) | 10 | `ERROR capa: default embedded rules not found!` | 2026-10-29 |
| capa | `capa -q -r ~/.local/share/capa-rules -j /usr/bin/true` (JSON summarized) | 0 | `format elf arch amd64 rules matched 3` | 2026-10-29 |
| floss | `floss --version` | 0 | `floss 3.2.0` | 2026-10-29 |
| floss | `floss -q --only static -- /usr/bin/true` | 0 | static strings, e.g. `/lib64/ld-linux-x86-64.so.2`, `nl_langinfo`, `__stack_chk_fail` | 2026-10-29 |
| yara | `yara --version` | 0 | `4.5.8` | 2026-10-29 |
| yara | `yara $T/rule.yar /usr/bin/true` (rule: `7F 45 4C 46` at 0) | 0 | `elf_magic /usr/bin/true` | 2026-10-29 |
| diec | `diec --version` | 0 | `die 3.21` | 2026-10-29 |
| diec | `diec /usr/bin/true` | 0 | `ELF64` / `Compiler: GCC((GNU) 16.2.1 20260810)` / `Library: GLIBC(ABI_DT_RELR)[DYN AMD64-64]` | 2026-10-29 |
| kaitai-struct-compiler | `kaitai-struct-compiler --version` | 0 | `kaitai-struct-compiler 0.11` | 2026-10-29 |
| kaitai-struct-compiler | `kaitai-struct-compiler -t python --outdir $T/ksc $T/hdr.ksy && ls $T/ksc` | 0 | `elf_magic.py` | 2026-10-29 |
| lief | `~/.local/share/re-pyenv/bin/python -c "import lief; b=lief.parse('/usr/bin/true'); print(lief.__version__, b.header.machine_type, len(b.sections))"` | 0 | `1.0.0-d05b3499b ARCH.X86_64 29` | 2026-10-29 |
| pefile | `python3 -c "import pefile; print(pefile.__version__)"` | 0 | `2024.8.26` | 2026-10-29 |
| pefile | `python3 -c "…pefile.PE('/usr/bin/true')…"` (catches PEFormatError) | 0 | `PEFormatError: 'DOS Header magic not found.'` (correct rejection of an ELF) | 2026-10-29 |
| capstone | `python3 -c "…Cs(X86,MODE_64).disasm(true[0x2590:0x25a0], 0x2590)…"` (0x2590 = entry point per `objdump -f`) | 0 | `5.0.7 ['endbr64 ', 'xor ebp, ebp', 'mov r9, rdx']` | 2026-10-29 |
| capstone | `cstool x64 '55 48 89 e5'` | 0 | `0  55  push rbp` / `1  48 89 e5  mov rbp, rsp` | 2026-10-29 |
| keystone | `python3 -c "…Ks(X86,MODE_64).asm('push rbp; mov rbp, rsp')…"` | 0 | `0.9.2 554889e5` | 2026-10-29 |
| keystone | `kstool x64 'push rbp; mov rbp, rsp'` | 0 | `push rbp; mov rbp, rsp = [ 55 48 89 e5 ]` | 2026-10-29 |
| unicorn | `python3 -c "…emulate 48c7c02a000000 (mov rax,42)…"` | 0 | `2.1.4 rax= 42` | 2026-10-29 |
| pwndbg | `pwndbg --version` | 0 | `GNU gdb (GDB) 18.1` | 2026-10-29 |
| pwndbg | `pwndbg -batch -ex 'file /usr/bin/true' -ex checksec` | 0 | `pwndbg: loaded 199 pwndbg commands.` … `RELRO: Full RELRO`, `Stack: Canary found`, `NX enabled`, `PIE enabled`, `SHSTK: Enabled`. Also printed: `~/.gdbinit:10: Error … module 'gdb' has no attribute 'printing'` (user's existing gdbinit, not changed) | 2026-10-29 |
| gef | `gdb -nx -batch -ex 'source /usr/share/gef/gef.py' -ex 'file /usr/bin/true' -ex checksec` | 0 | `GEF for linux ready…` / `93 commands loaded … GDB 18.1 … Python engine 3.14` / `Canary ✓ NX ✓ PIE ✓ Fortify ✘ RelRO Full` | 2026-10-29 |
| diffoscope | `diffoscope --version` | 0 | `diffoscope 331` | 2026-10-29 |
| diffoscope | `diffoscope --text - /usr/bin/true $T/true.copy` | 0 | (empty: identical files, as expected) | 2026-10-29 |
| diffoscope | `diffoscope --text - /usr/bin/true /usr/bin/false` | 0 (pipeline through grep) | `--- /usr/bin/true` / `+++ /usr/bin/false` / `│┄ File has been modified after NT_GNU_BUILD_ID has been applied.` | 2026-10-29 |
| checksec | `checksec --version` | 0 | `checksec version 3.2.0 (Built on 2026-06-21T19:27:36Z from Git SHA c8afc72)` | 2026-10-29 |
| checksec | `checksec file /usr/bin/true` (v3 syntax; `--file=` is the old 2.x form) | 0 | `Full RELRO  Canary Found  SHSTK & IBT  NX enabled  PIE E…` | 2026-10-29 |
| upx | `upx --version` | 0 | `upx 5.2.0` | 2026-10-29 |
| upx | `upx -t /usr/bin/true` (test only, no packing) | 2 | `upx: /usr/bin/true: NotPackedException: not packed by UPX` (expected for an unpacked binary) | 2026-10-29 |
| imhex | `imhex --version` (no pty) | 0 | (empty output) | 2026-10-29 |
| imhex | `script -qec 'imhex --version' /dev/null` (with a pty) | 0 | ASCII banner with `Version: 1.38.1`, `Commit: v1.38.X@76cf877` | 2026-10-29 |
| imhex | `script -qec 'imhex --hash sha256 /usr/bin/true' /dev/null` | 0 | `sha256(true) = 8398AF7D…AEF0662` (matches `sha256sum`: `8398af7d1f94a88be3303caa083616ad22a12783e4dfee0373298bc61aef0662`) | 2026-10-29 |
| cutter | `QT_QPA_PLATFORM=offscreen cutter --version` | 0 | `cutter 2.4.1-makepkg-a5f88d1` (GUI only, so no file probe) | 2026-10-29 |
| wabt | `wat2wasm --version` | 0 | `1.0.42` | 2026-10-29 |
| wabt | `wat2wasm $T/t.wat -o $T/t.wasm && wasm-objdump -x $T/t.wasm` | 0 | `t.wasm: file format wasm 0x1` … `Export[1]: - func[0] <f> -> "f"` | 2026-10-29 |
| binaryen | `wasm-opt --version` | 0 | `wasm-opt version 130` | 2026-10-29 |
| binaryen | `wasm-opt -O2 $T/t.wasm -o $T/t.opt.wasm && wasm-dis $T/t.opt.wasm` | 0 | `(module` … `(i32.const 42)` | 2026-10-29 |
| apktool | `apktool --version` | 0 | `3.0.3` | 2026-10-29 |
| apktool | `apktool --help` | 0 | `Apktool 3.0.3 - a tool for reengineering Android apk files` (no APK on the host to decode) | 2026-10-29 |
| ilspycmd | `ilspycmd --version` | 0 | `ilspycmd: 11.2.0.10050` | 2026-10-29 |
| ilspycmd | `ilspycmd -l c /usr/share/dotnet/sdk/*/dotnet.dll` | 0 | `Class <Module>` / `Class ToolPackageUninstaller` … | 2026-10-29 |
| rr | `rr --version` | 0 | `rr version 5.10.0` | 2026-10-29 |
| rr | `rr record -o $T/rrtrace /bin/true && rr ps $T/rrtrace` | 0 | trace dir created (`data events mmaps tasks version`); `rr ps`: `586944 -- 0 /bin/true`. This worked with `perf_event_paranoid=2` | 2026-10-29 |
| strace | `strace -V` | 0 | `strace -- version 7.2` | 2026-10-29 |
| strace | `strace -c -f /bin/true` | 0 | `% time seconds usecs/call calls errors syscall` … `mmap 8 calls` | 2026-10-29 |
| ltrace | `ltrace -V` | 0 | `ltrace 0.8.1` | 2026-10-29 |
| ltrace | `ltrace -c /bin/true` | 0 | `100.00 … 1 exit_group` | 2026-10-29 |
| patchelf | `patchelf --version` | 0 | `patchelf 0.19.2` | 2026-10-29 |
| patchelf | `patchelf --print-interpreter --print-needed /usr/bin/true` | 0 | `/lib64/ld-linux-x86-64.so.2` / `libc.so.6` | 2026-10-29 |
| pyinstxtractor-ng | `pyinstxtractor-ng --help` | 0 | `usage: pyinstxtractor-ng [-h] [-d] [-i] filename` | 2026-10-29 |
| pyinstxtractor-ng | `pyinstxtractor-ng /usr/bin/true` | 1 | `[!] Error: Missing cookie, unsupported pyinstaller version or not a pyinstaller archive` (correct negative) | 2026-10-29 |
| radare2 (pre-existing) | `r2 -v` | 0 | `radare2 6.2.2 +37485 abi:142 @ linux-x86_64` | 2026-10-29 |
| radare2 | `r2 -q -c 'iI~arch,bits,class' /usr/bin/true` | 0 | `arch x86` / `bits 64` / `class ELF64` (+ a `WARN: Relocs has not been applied` line) | 2026-10-29 |
| rizin (pre-existing) | `rizin -v` | 0 | `rizin 0.8.2 @ linux-x86-64` | 2026-10-29 |
| rizin | `rizin -q -c 'iI~arch' /usr/bin/true` | 0 | `arch x86` | 2026-10-29 |
| jadx (pre-existing) | `jadx --version` | 0 | `1.5.6` | 2026-10-29 |
| binwalk (pre-existing) | `binwalk /usr/bin/true` | 0 | `0  0x0  ELF binary, 64-bit shared object` | 2026-10-29 |
| unblob (pre-existing) | `unblob --version` | 0 | `26.6.4` | 2026-10-29 |
| objdump (pre-existing) | `objdump -f /usr/bin/true` | 0 | `/usr/bin/true: file format elf64-x86-64` (`start address 0x…2590`); `--version`: `GNU objdump (GNU Binutils) 2.47` | 2026-10-29 |
| gdb (pre-existing) | `gdb --version` | 0 | `GNU gdb (GDB) 18.1` | 2026-10-29 |

## Not installed / why

- **pycdc**: not in the official repos (AUR-only, skipped), and upstream (zrax/pycdc) publishes no release binaries. The only other route is a source build, which is not in the allowed channel order. Optional per the brief.
- **ksv (kaitai-struct-visualizer)**: not in the official repos (AUR-only, skipped). Upstream ships it as a Ruby gem, which is not an allowed channel. `kaitai-struct-compiler` is installed.
- **python-lief, imhex, detect-it-easy, kaitai-struct-compiler, apktool, rr, capa, floss**: none of these resolve from the official repos (the pacman packages are AUR-only). Each was installed from the next allowed channel instead (uv or official upstream release); see Installs.
- **pacman `cutter` (1.04)**: an unrelated TCP-connection cutter, so it was not installed. The Rizin GUI is `rz-cutter`.
- No package failed because of a stale sync DB. Every pacman install resolved from the current local DB.

## Caveats

- Run capa as `capa -r ~/.local/share/capa-rules …`. The uv install has no embedded rules: it exits 10 without `-r`.
- capa and floss run on uv-managed CPython 3.12. Their `python-flirt` dependency failed to build on the system Python 3.14.
- To use LIEF, run `~/.local/share/re-pyenv/bin/python`. The system `python3` cannot import it.
- The user's `~/.gdbinit` line 10 raises `module 'gdb' has no attribute 'printing'` when gdb or pwndbg starts. pwndbg still loads. The file was left unchanged.
- ImHex CLI subcommands only print when attached to a TTY. Use `script -qec '…' /dev/null` when running non-interactively.
