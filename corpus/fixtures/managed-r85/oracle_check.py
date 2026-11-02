#!/usr/bin/env python
"""oracle_check.py - verify the saved producer record against the fixture bytes.

Usage: python -B oracle_check.py <truth.json> <record.json> <fixture.dll>
Exit 0 iff every check passes. BYTE checks re-derive their expected value from
the fixture bytes with this file's own metadata parser (Q03: independent of the
record and of the generator); HYP checks are the pre-registered Q07 hypotheses
in truth.json (recorded whichever way they fall). Producer-internal ids are
checked for FORM only.
"""
import hashlib
import json
import struct
import sys
from pathlib import Path

RAW_HDR = 24  # #~ header: 8 reserved + 8 valid + 8 sorted
ROW_SIZES = {0x00: 10, 0x02: 14, 0x06: 14, 0x1A: 2, 0x1C: 8, 0x20: 22}
ROW_ORDER = [0x00, 0x02, 0x06, 0x1A, 0x1C, 0x20]
TABLE_NAMES = {0x00: "Module", 0x02: "TypeDef", 0x06: "MethodDef",
               0x1A: "ModuleRef", 0x1C: "ImplMap", 0x20: "Assembly"}


def parse(image):
    """Independent CLI-image parser: returns the derived facts dictionary."""
    assert image[:2] == b"MZ"
    e_lfanew, = struct.unpack_from("<I", image, 0x3C)
    cor_rva, cor_size = struct.unpack_from("<II", image, e_lfanew + 24 + 0x60 + 14 * 8)
    cor_foff = 0x200 + (cor_rva - 0x1000)
    _, _, _, md_rva, _, _, _ = struct.unpack_from("<IHHIIII", image, cor_foff)
    md_foff = 0x200 + (md_rva - 0x1000)
    sig, _, _, _, vlen = struct.unpack_from("<IHHII", image, md_foff)
    assert sig == 0x424A5342
    nstreams, = struct.unpack_from("<H", image, md_foff + 16 + vlen + 2)
    p = md_foff + 16 + vlen + 4
    streams = {}
    for _ in range(nstreams):
        so, ss = struct.unpack_from("<II", image, p)
        nm = image[p + 8:p + 24].split(b"\x00")[0]
        streams[nm.decode()] = (md_foff + so, ss)
        p += 8 + ((len(nm) + 1 + 3) & ~3)
    t, _ = streams["#~"]
    valid, = struct.unpack_from("<Q", image, t + 8)
    present = [bit for bit in ROW_ORDER if valid >> bit & 1]
    counts = struct.unpack_from("<%dI" % len(present), image, t + RAW_HDR)
    rows = {}
    off = t + RAW_HDR + 4 * len(present)   # counts block precedes the rows
    for bit, n in zip(present, counts):
        rows[bit] = (off, n)
        off += n * ROW_SIZES[bit]
    s, _ = streams["#Strings"]

    def cstr(idx):
        end = image.index(b"\x00", s + idx)
        return image[s + idx:end].decode("utf-8")

    il_row, il_n = rows[0x06]
    il_rva, il_impl, il_flags, il_name, il_sig, _ = struct.unpack_from(
        "<IHHHHH", image, il_row)
    pn_rva, pn_impl, pn_flags, pn_name, pn_sig, _ = struct.unpack_from(
        "<IHHHHH", image, il_row + 14)
    mr_row, _ = rows[0x1A]
    mr_idx, = struct.unpack_from("<H", image, mr_row)
    im_row, _ = rows[0x1C]
    mapping, fwd, imp_name, imp_scope = struct.unpack_from("<HHHH", image, im_row)
    body_foff = 0x200 + (il_rva - 0x1000)
    hdr = image[body_foff]
    assert (hdr & 0x03) == 0x02
    il_size = hdr >> 2
    il_bytes = image[body_foff + 1:body_foff + 1 + il_size]
    tok, = struct.unpack_from("<I", image, body_foff + 2)
    u, _ = streams["#US"]
    u_file = u
    ulen = image[u_file + 1]
    literal = image[u_file + 2:u_file + 2 + ulen - 1].decode("utf-16-le")
    b, _ = streams["#Blob"]

    def blob_entry(idx):
        blen = image[b + idx]
        assert blen < 0x80
        return blen, image[b + idx + 1:b + idx + 1 + blen]

    il_slen, il_sbytes = blob_entry(il_sig)
    pn_slen, pn_sbytes = blob_entry(pn_sig)
    g, _ = streams["#GUID"]
    gbytes = image[g:g + 16]          # GUID index 1 = heap bytes 0..16
    mvid = "%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%s" % (
        gbytes[3], gbytes[2], gbytes[1], gbytes[0], gbytes[5], gbytes[4],
        gbytes[7], gbytes[6], gbytes[8], gbytes[9],
        "".join("%02x" % x for x in gbytes[10:]))
    asm_row, _ = rows[0x20]
    _, maj, mi, bu, rv, _, _, an, _ = struct.unpack_from("<IHHHHIHHH", image, asm_row)
    td_row, _ = rows[0x02]
    ml_module, = struct.unpack_from("<H", image, td_row + 12)
    ml_probe, = struct.unpack_from("<H", image, td_row + 14 + 12)
    derived = {
        "fixture_sha": hashlib.sha256(image).hexdigest(),
        "byte_length": len(image),
        "mvid": mvid,
        "assembly_name": cstr(an),
        "assembly_version": "%d.%d.%d.%d" % (maj, mi, bu, rv),
        "table_row_counts": {TABLE_NAMES[k]: v[1] for k, v in rows.items()},
        "row_offsets": {"method1": il_row, "method2": il_row + 14,
                        "moduleref": mr_row, "implmap": im_row},
        "il_method": {"name": cstr(il_name), "rva": il_rva, "flags": il_flags,
                      "impl_flags": il_impl,
                      "body_file_offset": body_foff, "il_size": il_size,
                      "il_sha256": hashlib.sha256(il_bytes).hexdigest(),
                      "ldstr_token": "0x%08x" % tok,
                      "sig_len": il_slen,
                      "sig_sha256": hashlib.sha256(il_sbytes).hexdigest(),
                      "sig_conv": il_sbytes[0],
                      "sig_params": il_sbytes[1],
                      "sig_return": il_sbytes[2]},
        "pinv_method": {"name": cstr(pn_name), "rva": pn_rva, "flags": pn_flags,
                        "impl_flags": pn_impl,
                        "sig_len": pn_slen,
                        "sig_sha256": hashlib.sha256(pn_sbytes).hexdigest()},
        "implmap": {"mapping": mapping, "fwd": fwd,
                    "import_name": cstr(imp_name),
                    "scope_name": cstr(mr_idx)},
        "user_string": {"token": "0x%08x" % tok, "value": literal,
                        "file_offset": u_file + 1},
        "method_list": {"module": ml_module, "probe": ml_probe},
    }
    return derived


def dig(node, *path):
    for k in path:
        node = node[k]
    return node


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: oracle_check.py <truth.json> <record.json> <fixture.dll>",
              file=sys.stderr)
        return 2
    truth = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    rec = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    image = Path(sys.argv[3]).read_bytes()
    d = parse(image)
    norm = rec.get("normalized_result") or {}
    hyp = truth["hyp"]
    checks = []

    def add(name, got, want):
        checks.append((name, got, want))

    if rec.get("operation") == hyp["members_operation"]:
        m = norm["methods"]
        il = d["il_method"]
        m0 = m[0]
        add("op", rec.get("operation"), hyp["members_operation"])
        add("provider.id", dig(rec, "provider", "id"), hyp["provider_id"])
        add("subject.sha256==bytes", dig(rec, "subject", "digest", "sha256"),
            d["fixture_sha"])
        add("bytes.len", norm["artifact"]["byte_length"], d["byte_length"])
        add("module.name", dig(norm, "module", "name"), truth["module_name"])
        add("module.mvid", dig(norm, "module", "mvid"), d["mvid"])
        add("assembly.name", dig(norm, "assembly", "name"), d["assembly_name"])
        add("assembly.version", str(dig(norm, "assembly", "version")),
            d["assembly_version"])
        trc = {k: v for k, v in dig(norm, "metadata", "table_row_counts").items()}
        add("metadata.table_row_counts", trc, d["table_row_counts"])
        add("metadata.status", dig(norm, "metadata", "status"), hyp["metadata_status"])
        add("methods.count", len(m), 2)
        add("m0.token", m0["token"], "0x06000001")
        add("m0.name", m0["name"], il["name"])
        add("m0.rva", m0["rva"], il["rva"])
        add("m0.row_offset", m0["row_offset"], d["row_offsets"]["method1"])
        add("m0.flags", m0["flags"], il["flags"])
        add("m0.impl_flags", m0["impl_flags"], il["impl_flags"])
        add("m0.body.status", dig(m0, "body", "status"), hyp["body_status"])
        add("m0.body.format", dig(m0, "body", "header_format"), hyp["body_format"])
        add("m0.body.file_offset", dig(m0, "body", "file_offset"),
            il["body_file_offset"])
        add("m0.body.il_size", dig(m0, "body", "il_size"), il["il_size"])
        add("m0.body.il_sha256", dig(m0, "body", "il_sha256"), il["il_sha256"])
        add("m0.body.opcode_counts", dig(m0, "body", "opcode_counts"),
            hyp["opcode_counts"])
        anchors = dig(m0, "body", "anchors")
        add("m0.anchor0", [anchors[0]["il_offset"], anchors[0]["opcode"],
                           anchors[0]["operand"]],
            [0, "ldstr", il["ldstr_token"]])
        add("m0.anchor1", [anchors[1]["il_offset"], anchors[1]["opcode"]],
            [5, "ret"])
        add("m0.sig.raw_length", dig(m0, "signature", "raw_length"), il["sig_len"])
        add("m0.sig.raw_sha256==bytes", dig(m0, "signature", "raw_sha256"),
            il["sig_sha256"])
        add("m0.sig.parse_status", dig(m0, "signature", "parse_status"),
            hyp["sig_parse_status"])
        add("m0.sig.conv", dig(m0, "signature", "calling_convention"),
            "default" if il["sig_conv"] == 0x00 else "?")
        add("m0.sig.params", dig(m0, "signature", "parameter_count"),
            il["sig_params"])
        add("m0.sig.return", dig(m0, "signature", "return_type"),
            {0x0E: "string", 0x01: "void"}[il["sig_return"]])
        m1 = m[1]
        pn = d["pinv_method"]
        add("m1.token", m1["token"], "0x06000002")
        add("m1.name", m1["name"], pn["name"])
        add("m1.rva", m1["rva"], pn["rva"])
        add("m1.flags", m1["flags"], pn["flags"])
        add("m1.impl_flags", m1["impl_flags"], pn["impl_flags"])
        add("m1.body.status", dig(m1, "body", "status"), "absent")
        us = norm["user_strings"]
        add("us.state", us["state"], hyp["us_state"])
        add("us.literals.count", len(us["literals"]), hyp["user_string_literal_count"])
        add("us.lit.value", us["literals"][0]["value"], d["user_string"]["value"])
        add("us.lit.token", us["literals"][0]["token"], d["user_string"]["token"])
        add("us.lit.offset", us["literals"][0]["offset"],
            d["user_string"]["file_offset"])
        add("us.issues", us["issues"], [])
        add("coverage.state", norm["coverage"]["state"], hyp["coverage_state"])
        add("confidence", rec.get("confidence"), hyp["confidence"])
        add("authority", rec.get("authority"), hyp["authority"])
        add("evidence_id.form", bool(rec.get("evidence_id")), True)
    elif rec.get("operation") == hyp["artifact_operation"]:
        add("op", rec.get("operation"), hyp["artifact_operation"])
        add("provider.id", dig(rec, "provider", "id"), hyp["provider_id"])
        add("subject.sha256==bytes", dig(rec, "subject", "digest", "sha256"),
            d["fixture_sha"])
        add("bytes.len", norm["artifact"]["byte_length"], d["byte_length"])
        add("classification.status", dig(norm, "classification", "status"),
            hyp["classification_status"])
        add("classification.implementation",
            dig(norm, "classification", "implementation"), hyp["implementation"])
        add("classification.managed_architecture",
            dig(norm, "classification", "managed_architecture"),
            hyp["managed_architecture"])
        evs = dig(norm, "classification", "evidence")
        add("classification.evidence.codes",
            [e.get("code") for e in evs], hyp["evidence_codes"])
        add("classification.evidence.file_offsets",
            [e.get("file_offset") for e in evs],
            [hyp["cor_header_file_offset"], hyp["cor_flags_file_offset"]])
        add("metadata.status", dig(norm, "metadata", "status"), hyp["metadata_status"])
        add("metadata.stream_names", sorted(dig(norm, "metadata", "stream_names")),
            sorted(hyp["stream_names"]))
        trc = dig(norm, "metadata", "table_row_counts")
        add("metadata.table_row_counts", trc, d["table_row_counts"])
        add("module.name", dig(norm, "module", "name"), truth["module_name"])
        add("module.mvid", dig(norm, "module", "mvid"), d["mvid"])
        add("assembly.name", dig(norm, "assembly", "name"), d["assembly_name"])
        add("assembly.version", str(dig(norm, "assembly", "version")),
            d["assembly_version"])
        add("coverage.state", norm["coverage"]["state"], hyp["coverage_state"])
        add("confidence", rec.get("confidence"), hyp["confidence"])
        add("authority", rec.get("authority"), hyp["authority"])
        add("evidence_id.form", bool(rec.get("evidence_id")), True)
    elif rec.get("operation") == hyp["boundaries_operation"]:
        add("op", rec.get("operation"), hyp["boundaries_operation"])
        add("provider.id", dig(rec, "provider", "id"), hyp["provider_id"])
        add("subject.sha256==bytes", dig(rec, "subject", "digest", "sha256"),
            d["fixture_sha"])
        add("bytes.len", norm["artifact"]["byte_length"], d["byte_length"])
        im = d["implmap"]
        mrs = norm["module_refs"]
        add("module_refs.count", len(mrs), 1)
        add("mr.name", mrs[0]["name"], im["scope_name"])
        add("mr.token", mrs[0]["token"], "0x1a000001")
        add("mr.row_offset", mrs[0]["row_offset"], d["row_offsets"]["moduleref"])
        pi = norm["pinvoke_imports"]
        add("pi.count", len(pi), 1)
        add("pi.mapping_flags", pi[0]["mapping_flags"], im["mapping"])
        add("pi.import_name", pi[0]["import_name"], im["import_name"])
        add("pi.import_scope_name", pi[0]["import_scope_name"], im["scope_name"])
        add("pi.member_token", pi[0]["member_token"],
            "0x%08x" % (0x06000000 | (im["fwd"] >> 1)))
        add("pi.member_kind", pi[0]["member_kind"], "method")
        add("pi.member_name", pi[0]["member_name"], d["pinv_method"]["name"])
        cs = {0: "notspec", 2: "ansi", 4: "unicode", 6: "auto"}[im["mapping"] & 6]
        cc = {0x00: "winapi", 0x0100: "winapi", 0x0200: "cdecl",
              0x0300: "stdcall"}[im["mapping"] & 0x0700]
        add("pi.char_set", pi[0]["char_set"], cs)
        add("pi.call_convention", pi[0]["call_convention"], cc)
        add("pi.no_mangle", pi[0]["no_mangle"], bool(im["mapping"] & 1))
        add("pi.supports_last_error", pi[0]["supports_last_error"],
            bool(im["mapping"] & 0x40))
        add("pi.verification", pi[0]["verification"], hyp["verification"])
        ni = norm["native_implementations"]
        add("ni.count", len(ni), 1)
        add("ni.token", ni[0]["token"], "0x06000002")
        add("ni.name", ni[0]["name"], d["pinv_method"]["name"])
        add("ni.rva", ni[0]["rva"], d["pinv_method"]["rva"])
        add("ni.flags", ni[0]["flags"], d["pinv_method"]["flags"])
        add("ni.impl_flags", ni[0]["impl_flags"], d["pinv_method"]["impl_flags"])
        add("ni.boundary_kind", ni[0]["boundary_kind"], hyp["boundary_kind"])
        add("ni.code_type", ni[0]["code_type"], hyp["code_type"])
        add("ni.managed_kind", ni[0]["managed_kind"], hyp["managed_kind"])
        add("ni.pinvoke_declared", ni[0]["pinvoke_declared"], True)
        add("summary.module_refs", dig(norm, "summary", "module_ref_count"),
            hyp["module_ref_count"])
        add("summary.pinvokes", dig(norm, "summary", "pinvoke_import_count"),
            hyp["pinvoke_import_count"])
        add("summary.native_impls", dig(norm, "summary", "native_implementation_count"), 1)
        add("cli_native.il_only", dig(norm, "cli_native", "il_only"), True)
        add("metadata.status", dig(norm, "metadata", "status"), hyp["metadata_status"])
        add("coverage.state", norm["coverage"]["state"], hyp["coverage_state"])
        add("confidence", rec.get("confidence"), hyp["confidence"])
        add("authority", rec.get("authority"), hyp["authority"])
        add("evidence_id.form", bool(rec.get("evidence_id")), True)
    else:
        print(f"FAIL operation {rec.get('operation')!r} is neither expected operation")
        return 1

    ok = True
    for name, got, want in checks:
        good = got == want
        ok = ok and good
        print(f"{'OK ' if good else 'FAIL'} {name}: got={got!r}"
              + ("" if good else f" want={want!r}"))
    print(f"ORACLE {'OK' if ok else 'FAILED'} "
          f"({sum(1 for _, g, w in checks if g == w)}/{len(checks)} checks)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
