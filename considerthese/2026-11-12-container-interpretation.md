# Revenger: container interpretation before semantic claims

Four primary-source reading paths turn a recognizable file signature into a bounded interpretation process. Each exercise is proposed and unperformed. These plans do not authorize training, assimilation, live-target capture, or testing third-party systems.

## Why these sources belong together

A signature identifies a candidate format. Interpreting its contents may still require section-local state, an external schema, or metadata stored elsewhere in the file. The progression below moves from packet timestamps to message fields, schema-governed blocks, and columnar files. The common question is what additional evidence makes a decoded value meaningful.

The live registry and 16 existing considerthese files were inspected on 2026-11-12. In a bounded comparison with 383 distinct accessible curation artifacts, pcapng appeared only in a general tool-capability discussion; Parquet and Avro did not appear. Existing archive, compression, JSON, CBOR, TIFF, PNG, and memory-format notes remain useful. These four case designs add different interpretation dependencies rather than replacing those lessons.

## 1. Pcapng timestamps depend on section and interface state

**Primary source.** The IETF OPSAWG authors' [pcapng draft 06](https://www.ietf.org/archive/id/draft-ietf-opsawg-pcapng-06.html), dated 19 September 2026, sections 4.1–4.3. Use this fixed Internet-Draft, not a claim that pcapng is a finalized RFC. Draft 05 was discovered first and excluded from the selected reading because draft 06 was available.

**Evidence and transition.** Section Header Blocks establish byte ordering. Interface IDs are local to their section; the same number can identify different interfaces after a new section begins. Enhanced Packet Block timestamps combine upper and lower 32-bit words into one count. Their unit and offset come from the referenced interface's options, not from a universal seconds/microseconds pair. Identical integer fields can therefore denote different times in different interface contexts.

**Bounded first-hand exercise, unperformed.** Author a synthetic capture with two sections, each with one Interface Description Block and one Enhanced Packet Block. Use interface ID zero in both sections, opposite byte ordering, and distinct timestamp resolutions. Include only an invented packet payload. Prepare variants with the resolution option absent, with a binary-power resolution, and with a nonzero timestamp offset. Keep the full set below eight files and one MiB.

**Controls and expected evidence.** A decoder that retains interface state across section boundaries should disagree with the specification worksheet. A timestamp interpreted as two decimal components should also disagree. Add one invalid interface reference and require a precise refusal or an explicit unresolved interpretation. Compare the worksheet with a locally available capture reader; no network capture or packet transmission is needed.

**Report criterion.** For every packet retain the section number, interface index, endianness, raw high/low words, resolution encoding, offset, and derived time. Resolution is not clock accuracy or synchronization. A draft-conforming conversion cannot establish that two real capture hosts had aligned clocks. Iterate only after explaining a reader discrepancy or a previously uncovered option boundary.

## 2. Protobuf wire types leave semantic alternatives open

**Primary source.** Protocol Buffers' [Encoding guide](https://protobuf.dev/programming-guides/encoding/), “Message Structure,” “Length-Delimited Records,” “Repeated Elements,” “Last One Wins,” and “Field Order.” The selected page assumes Edition 2023 or later in its examples; record the actual compiler/runtime edition in a later exercise.

**Evidence and transition.** A wire record exposes its field number and wire type. It does not reveal the source field name or full declared type. A length-delimited payload can represent text, bytes, a nested message, or packed scalars. Repeated encodings, duplicate singular fields, and ordering rules complicate a one-to-one association between byte sequences and application objects. Syntactically parsing a plausible nested message is therefore insufficient to establish that the producer intended a nested message.

**Bounded first-hand exercise, unperformed.** Write two original schemas whose field 1 is respectively bytes and an embedded message. Construct one tiny wire payload valid under both. Decode it with each schema and retain both interpretations. Next, create two serializations of an equivalent message with different permitted field orders, plus a duplicate singular-field case and a packed/expanded scalar case. Keep each payload under 256 bytes and the family under eight files.

**Controls and expected evidence.** The oracle is the authored schema and construction record, not the decoder's prettiest output. Include a truncated length-delimited field that must not become a successful complete decode. Compare the raw byte hash separately from the schema-specific decoded value. Do not equate deterministic serialization within one documented implementation with universal canonical encoding across implementations.

**Report criterion.** Preserve the schema hash, edition, runtime version, raw field order, duplicate handling, and undecoded fields. Report “compatible with this schema” unless producer evidence establishes the schema binding. Expand to another runtime only after the first report explains ambiguity and incomplete input correctly. Do not infer package identity, message intent, or maliciousness from a speculative schema alone.

## 3. Avro distinguishes embedded schema from schema fingerprint

**Primary source.** Apache Avro's [1.12.0 specification](https://avro.apache.org/docs/1.12.0/specification/), “Single-object encoding,” “Object Container Files,” “Schema Resolution,” and “Parsing Canonical Form for Schemas.” These are different mechanisms, not alternate names for one wrapper.

**Evidence and transition.** Object container files carry the writer schema in metadata and organize data into blocks with a per-file synchronization marker. Single-object encoding carries a marker and a CRC-64-AVRO schema fingerprint before the encoded object, so the reader still needs the corresponding schema. Reader/writer resolution can apply defaults or omit fields according to the two schemas. Successful resolution is not evidence that the original bytes physically contained every field in the resulting object. A sync marker or CRC fingerprint is not a cryptographic authenticity claim.

**Bounded first-hand exercise, unperformed.** Author a two-field record schema and three records. Produce one small object container file and one single-object encoding for each record using an already available Avro implementation. Keep a local fingerprint-to-schema table with no external registry access. Supply a second reader schema adding a field with a default, and a third incompatible reader schema. Use no compression first so byte boundaries stay inspectable.

**Controls and expected evidence.** Withhold the fingerprint's schema mapping in one single-object case. Keep “schema unavailable” separate from “data corrupt.” For container copies, truncate one block and modify one sync marker without executing embedded content. The parser may reject them, but no particular diagnostic is assumed. Check whether an added reader-default value came from resolution rather than from a stored field.

**Report criterion.** Retain container kind, writer and reader schema hashes, schema fingerprint, block count/size, codec, sync-marker observations, and original versus synthesized fields. Acceptance requires explaining at least one valid schema evolution and one refusal without conflating missing schema with bad payload. Only then add a codec or a second implementation. A successful toy round trip does not validate every Avro logical type or schema-evolution rule.

## 4. Parquet footer metadata does not certify every page

**Primary sources.** Apache Parquet's [File Format](https://parquet.apache.org/docs/file-format/) overview and [Encryption](https://parquet.apache.org/docs/file-format/data-pages/encryption/) specification. The format overview explicitly pairs its description with the Thrift definitions. The [upstream encryption specification, section 5.4](https://github.com/apache/parquet-format/blob/master/Encryption.md) explicitly describes the PARE marker. The encryption document distinguishes encrypted-footer and plaintext-footer modes; it is not a reason to treat every non-PAR1 file as an ordinary corrupt Parquet file.

**Evidence and transition.** In the ordinary layout, file metadata follows the column data and a footer length permits locating it from the end. Reading metadata can enumerate row groups without reading all their pages. Encryption adds another interpretation boundary, including the PARE magic for encrypted-footer files. Thus “metadata read succeeded,” “a selected projection decoded,” and “every requested row group and column decoded” are different coverage statements.

**Bounded first-hand exercise, unperformed.** Create a four-row, two-column local file with two row groups and no sensitive data. Record its schema and expected values independently. Request only column A, then both columns, recording which row groups and pages the reader actually accesses where observable. Make a footer-truncated copy and a copy with one deliberately corrupted data page in column B. Bound parsing time and output size. No claim is made that a particular reader will defer that page or expose precise read instrumentation.

**Controls and expected evidence.** Compare metadata-only, projected, and full-data reads. If all modes fail early, retain that result rather than forcing the desired demonstration. Separately classify an encrypted-footer signature as requiring the matching encryption context; do not fabricate a decryption success, acquire keys, or conflate missing authorization with corruption. Any metadata-only copy retained for analysis remains a derived artifact, not the original data file.

**Report criterion.** State the footer bounds, file size, selected columns/row groups, bytes or pages actually inspected when measurable, and all checks the reader performed. A complete claim needs a stated coverage denominator. Advance only if the report exposes a meaningful difference between structural inventory and content validation, or documents why the tested reader does not make that distinction observable.

## Report template and stopping rules

1. Question and permitted local fixture scope.
2. Source edition, retrieval date, implementation version, and input hashes.
3. Predicted structural interpretation and one falsifying control.
4. First outputs, including failures and missing capabilities.
5. Byte range or metadata dependency for every conclusion.
6. Observation, inference, and unresolved alternatives in separate fields.
7. A single proposed next experiment and the fact that would make it unnecessary.

Each family is limited to eight toy fixtures, 20 MiB retained output, and ten minutes of local processing. Treat a parser crash, timeout, or missing codec as a result to diagnose, not as evidence of a security vulnerability. A second reviewer should decode one held-out fixture from the source rules without seeing the author's proposed semantic label. Stop expanding a family after two iterations that add no corrected boundary, new control, or narrower claim.

## Rights and reuse

The pcapng draft carries IETF Trust copyright and [BCP 78 license terms](https://trustee.ietf.org/license-info); extracted code components have additional notice conditions. No draft code is copied here. Protocol Buffers' [software license](https://github.com/protocolbuffers/protobuf/blob/main/LICENSE) is the three-clause BSD-style license; the web guide's prose reuse license was not separately established, so this note links and briefly paraphrases it rather than redistributing it. Apache [Avro](https://github.com/apache/avro/blob/main/LICENSE.txt) and [Parquet format](https://github.com/apache/parquet-format/blob/master/LICENSE) provide Apache 2.0 licenses; preserve notices when reusing their implementation or specification material. The proposed fixture contents are original, not borrowed captures or production data.

Destination: VeigaPunk/shokunin-binary-forensics, main, considerthese/2026-11-12-container-interpretation.md.
