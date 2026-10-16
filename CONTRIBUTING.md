# Contributing

Submit an issue or pull request to correct a capability, document a plan restriction or add a relevant business system. No prior contact is needed.

1. Edit `data/integrations.json`, the canonical source. Keep existing system and source IDs stable.
2. Cite a publicly accessible **official vendor** document for each technical claim. Add its URL, title and the date you actually reviewed it. Avoid partner marketing pages as proof of vendor entitlements.
3. Scope the product, API version, country and record type. Distinguish core API access, outbound webhooks, automation actions, streaming events and third-party connectors.
4. Use `not_confirmed`/`null` when evidence is insufficient. Do not infer absence from silence, or entitlement from an endpoint merely existing.
5. Keep documentation evidence separate from connection testing. To set `verification.status` to `tested`, include `tested_at`, `test_scope` and public, sanitised evidence URLs describing environment, plan, auth method, exact operations, expected/actual results and limitations. A documentation review, website test or mocked API does not qualify.
6. Never upload credentials, customer records, personal data or private screenshots. Use synthetic records in an authorised test environment. Do not change live accounts just to contribute evidence.
7. Run `python3 scripts/export.py` and `python3 -m unittest discover -s tests`. Include generated CSV changes. Update dataset version and the relevant entry dates only when reviewed.

By submitting original contributions you agree to distribute the catalogue under CC BY 4.0 and code under MIT. Retain source attribution and identify substantive corrections in the pull request. Maintainers check evidence before merging. Commercial integrations and prices can change; a passing data validator does not prove vendor capability.
