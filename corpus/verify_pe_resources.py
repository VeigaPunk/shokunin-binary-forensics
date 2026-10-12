#!/usr/bin/env python3
"""Saved PE resource relation check. No PE execution."""
import copy
import hashlib
import json
import sys
from pathlib import Path

CORPUS = Path(__file__).resolve().parent
FIXTURE = CORPUS / "fixtures/pe-r27/fixture.exe"
TRUTH = CORPUS / "fixtures/pe-r27/truth.json"
EVIDENCE = CORPUS / "live/runs/round-27/inspection.json"
EXPECTED_ID = "ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef"


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def verify(evidence):
    blob = FIXTURE.read_bytes()
    truth = json.loads(TRUTH.read_text())
    digest = hashlib.sha256(blob).hexdigest()
    payload = blob[truth["payload_file_offset"]:truth["payload_file_offset"] + truth["payload_bytes"]]
    require(digest == truth["sha256"] and len(blob) == truth["size"], "fixture identity")
    require(payload == truth["payload_ascii"].encode("ascii") and
            hashlib.sha256(payload).hexdigest() == truth["payload_sha256"], "authored payload")
    require(blob[0:2] == b"MZ" and blob[truth["resource_directory_file_offset"]:truth["resource_directory_file_offset"] + 2] != b"",
            "pe carrier")
    require(evidence["evidence_id"] == EXPECTED_ID and evidence["operation"] == "inspect_pe_resources" and
            evidence["subject"]["digest"]["sha256"] == digest, "saved Evidence identity")
    result = evidence["normalized_result"]
    require(result["artifact"]["sha256"] == digest and result["artifact"]["bytes"] == len(blob) and
            result["format"] == "pe32" and result["machine"] == truth["machine"], "artifact mismatch")
    directory = result["directory"]
    require(directory["rva"] == truth["resource_directory_rva"] and
            directory["location"]["offset"] == truth["resource_directory_file_offset"] and
            directory["location"]["bytes"] == truth["resource_directory_bytes"], "directory mismatch")
    resources = result["resources"]
    require(len(resources) == 1 and result["coverage"]["resources"] == 1, "wrong resource count")
    item = resources[0]
    require(item["type"]["kind"] == "id" and item["type"]["id"] == truth["type_id"] and
            item["name"]["kind"] == "id" and item["name"]["id"] == truth["name_id"] and
            item["language"]["kind"] == "id" and item["language"]["id"] == truth["language_id"],
            "type/name/language mismatch")
    reported = item["payload"]
    require(reported["location"]["offset"] == truth["payload_file_offset"] and
            reported["location"]["bytes"] == truth["payload_bytes"] and
            reported["sha256"] == truth["payload_sha256"] and
            reported["sha256"] == hashlib.sha256(payload).hexdigest(),
            "payload relation mismatch")
    require(evidence["confidence"] == "observed" and result["icon_groups"] == [], "unexpected claim shape")
    return "1/1 RT_RCDATA name 1 language 1033 maps to authored payload"


def main():
    evidence = json.loads(EVIDENCE.read_text())
    print("POSITIVE", EXPECTED_ID, verify(evidence))
    if "--self-test" in sys.argv:
        altered = copy.deepcopy(evidence)
        altered["normalized_result"]["resources"][0]["payload"]["sha256"] = "0" * 64
        try:
            verify(altered)
        except ValueError as error:
            print("NEGATIVE REJECTED", error)
        else:
            raise AssertionError("mutated payload hash accepted")


if __name__ == "__main__":
    main()
