#!/usr/bin/env python3
"""Fixture-scoped EVM Evidence consistency check; no bytecode execution."""
import copy
import hashlib
import json
import sys
from pathlib import Path

CORPUS = Path(__file__).resolve().parent
FIXTURE = CORPUS / "fixtures/evm-r19"
EVIDENCE = CORPUS / "live/runs/round-19/inspection.json"
EXPECTED_ID = "ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42"


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def verify(evidence):
    carrier = (FIXTURE / "fixture.hex").read_bytes()
    truth = json.loads((FIXTURE / "truth.json").read_text())
    require(carrier.startswith(b"0x") and carrier.endswith(b"\n"), "carrier encoding")
    decoded = bytes.fromhex(carrier[2:-1].decode("ascii"))
    digest = lambda data: hashlib.sha256(data).hexdigest()
    require(digest(carrier) == truth["carrier_sha256"] and
            digest(decoded) == truth["decoded_sha256"] and
            len(decoded) == truth["decoded_size"] and truth["encoding"] == "hex",
            "fixture identity")
    opcode = truth["push4_opcode_offset"]
    immediate = truth["selector_immediate_offset"]
    require(opcode + 1 == immediate and truth["selector_immediate_length"] == 4 and
            decoded[opcode] == 0x63 and decoded[immediate:immediate + 4].hex() == truth["selector_push4"] and
            decoded[immediate + 4] == 0x14 and decoded[immediate + 5] == 0x60 and
            decoded[immediate + 7] == 0x57, "fixture selector comparison")
    result = evidence["normalized_result"]
    require(evidence["evidence_id"] == EXPECTED_ID and evidence["operation"] == "inspect_evm_interface" and
            evidence["subject"]["digest"]["sha256"] == digest(carrier) and
            evidence["parameters"]["encoding"] == result["artifact"]["encoding"] == "hex",
            "saved Evidence identity")
    require(result["artifact"]["sha256"] == digest(carrier) and
            result["artifact"]["bytes"] == len(carrier) and
            result["bytecode"]["sha256"] == digest(decoded) and
            result["bytecode"]["bytes"] == len(decoded) and
            result["bytecode"]["hex"] == decoded.hex(), "carrier/decoded mismatch")
    functions = result["functions"]
    require(len(functions) == 1 and len(evidence["raw_result"]["functions"]) == 1,
            "wrong candidate count")
    function = functions[0]
    target = function["bytecode_offset"]
    require(function["selector"] == "0x" + truth["selector_push4"] and
            evidence["raw_result"]["functions"][0]["selector"] == truth["selector_push4"] and
            evidence["raw_result"]["functions"][0]["bytecodeOffset"] == target and
            target == immediate + 9 and target < len(decoded) and decoded[target] == 0x5b and
            decoded[immediate + 6] == target and target != opcode and target != immediate,
            "candidate destination mismatch")
    require(result["evidence_kind"] == "inferred" and evidence["confidence"] == "inferred" and
            result["discovery_completeness"] == "unknown" and
            result["runtime_execution"] == "not-performed", "inference limits")
    return "1/1 selector candidate and two digests; destination 16 != PUSH4 6; inferred only"


def main():
    evidence = json.loads(EVIDENCE.read_text())
    print("POSITIVE", EXPECTED_ID, verify(evidence))
    if "--self-test" in sys.argv:
        altered = copy.deepcopy(evidence)
        altered["normalized_result"]["functions"][0]["bytecode_offset"] = 6
        try:
            verify(altered)
        except ValueError as error:
            print("NEGATIVE REJECTED", error)
        else:
            raise AssertionError("selector opcode offset mistaken for destination")


if __name__ == "__main__":
    main()
