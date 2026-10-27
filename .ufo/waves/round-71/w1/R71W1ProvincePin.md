VERDICT — 6.5.0 correction justified for the route pin; PROVINCE.md's 6.4.0 is stale relative to S049.

Evidence (read-only, 2026-10-27):
- `PROVINCE.md:19` says: “else `npx -y rea-agents@6.5.0`” — correction: this is in fact 6.5.0, not 6.4.0. (The current province pin is already 6.5.0.)
- `corpus/SOURCES.md:63` S049 URL names `rea-agents-6.5.0`; its scope is documented `inspect_android_package` route inputs/outputs only, explicitly not host provider execution or fixture bytes.
- `corpus/SOURCES.md:53,57` S039/S043 likewise identify the Android reference at tag 6.5.0.

Conclusion: comparison premise “PROVINCE route pin 6.4.0 versus records/S049 6.5.0” is not supported by current source: PROVINCE line 19 explicitly pins 6.5.0. So no PROVINCE correction is justified. If the concern instead is another retained 6.4.0 route/source record, that is a distinct issue; these files do not establish it. The 6.5.0 S049 basis is consistent with Province's stated package pin.
