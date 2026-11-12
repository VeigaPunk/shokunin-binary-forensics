# Revenger: compatible framing does not supply a missing dictionary

[RFC 8878](https://www.rfc-editor.org/rfc/rfc8878.html), February 2021, section 5, leaves Zstandard dictionaries outside compressed content and their delivery unspecified.

[RFC 9842](https://www.rfc-editor.org/rfc/rfc9842.html), September 2025, sections 5–6, defines HTTP's dcz encoding and dictionary negotiation. Its 40-byte header is a Zstandard skippable frame containing the external dictionary's 32-byte SHA-256 hash. The dictionary bytes remain external.

This assigns protocol meaning to framing a generic decoder can skip. It extends the earlier skippable-metadata note: preserving an unexplained span becomes identifying a specific decoding dependency. This is a transport refinement, not a replacement compression algorithm.

For captured artifacts, record the advertised dictionary hash and whether matching bytes were retained. Header recognition alone does not establish standalone recoverability. The hash neither supplies the dictionary nor authenticates its producer.

The sources are Informational and Standards Track respectively. Their notices apply publication-date IETF Trust terms. Original commentary; no code, decoding, training or assimilation.

Destination: VeigaPunk/shokunin-binary-forensics, main, considerthese/2026-11-11-dictionary-dependency-binding.md.
