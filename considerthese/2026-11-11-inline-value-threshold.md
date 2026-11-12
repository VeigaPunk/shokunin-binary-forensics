# Revenger: a wider field can stop being a pointer

LibTIFF's [BigTIFF design](https://libtiff.gitlab.io/libtiff/specification/bigtiff.html) contrasts classic TIFF's four-byte inline threshold with BigTIFF's eight-byte threshold. Values fitting the threshold occupy the directory entry itself; larger values reside elsewhere. The selection rule persists.

Thus, a six-byte tag payload is referenced in classic TIFF but inline in BigTIFF. An inferred illustration, not a fixture. Determine format, datatype and count before treating the value field as an address.

The [4.0.0 release account](https://libtiff.gitlab.io/libtiff/releases/v4.0.0.html) records BigTIFF support while retaining classic TIFF as the writing default. It also warns that the internal directory-entry structure no longer exactly represents either disk layout.

Documentation snapshot 4.7.2; no parser tested. Unassimilated. Design prose contains inconsistent entry offsets; none are relied upon here.

Original commentary; no copied examples. [License](https://libtiff.gitlab.io/libtiff/project/license.html) permits documentation reuse with retained notices and advertising restrictions.

Reviewed 2026-11-11. Destination: VeigaPunk/shokunin-binary-forensics, main, considerthese/2026-11-11-inline-value-threshold.md.
