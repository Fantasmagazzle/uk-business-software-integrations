# Data dictionary

Version 1.0.0. UTF-8, ISO `YYYY-MM-DD` dates. Join tables on `id` (systems) = `system_id` (other tables), and source `id` = `source_id` / each `source_ids` member.

## Canonical JSON

- `schema_version`: shape of this dataset. `dataset_version`: content release date.
- `canonical_url`, `publisher`, `licence`: attribution and reuse metadata.
- `selection_method`, `evidence_policy`: sampling and evidence limitations.
- `systems[].id`: stable, lowercase URL slug. `name`, `category`, `product_scope`: product identity and boundaries.
- `api.status`: `documented`, `not_confirmed` or `unavailable`; `style`: REST/GraphQL for this scoped entry. Availability never guarantees all operations.
- `plans.status`: `documented` (named editions in reviewed sources), `conditional` (known entitlement/add-on/contract condition), `not_confirmed` (minimum commercial tier not established). `minimum_plan` is a human-readable summary, not a comparable price or Boolean. `notes` carries qualifications.
- `webhooks.status`: `http` (documented outbound HTTP notifications), `conditional` (known eligibility restriction), `event_stream` (streaming alternative, not HTTP webhook), `not_confirmed` (unknown), `unavailable` (explicit official evidence of absence). Always read `notes`; HTTP can still require scopes/app setup.
- `authentication.methods`, `notes`: auth methods and required access for the scoped API. Not credentials.
- `records[]`: selected entity groups, not an exhaustive endpoint inventory. `read`, `create`, `update` are `true` (documented), `false` (documented unsupported in scope), `null` (not assessed/confirmed). Notes qualify fields, state and permissions.
- `limitations[]`: documented restrictions. Numeric quotas are deliberately prose because units and scopes differ across products. Do not rank vendors by these numbers.
- `source_ids`: references supporting that fact. They resolve within the entry’s `sources` list.
- `ai_use_case`: Generativ editorial example, not a tested capability, customer case study or vendor claim.
- `last_checked`: date documentation was reviewed; not the vendor publication date or a live test timestamp.
- `verification.status`: `not_tested` or `tested`; tested entries require a date, scope and evidence links. A scoped test does not validate every capability or every tenant.
- `sources[].id`, `title`, `url`, `checked_at`: official reference identity and review date. Linked content may change after review.

## CSVs

`systems.csv` flattens the identity, API, plans, webhook and auth objects into correspondingly prefixed columns. `authentication_methods` and `limitations` use ` | ` separators. `ai_use_case_editorial` labels examples explicitly. `tested_at` and `test_scope` are blank when not tested. `source_count` counts references, not independent test results. `detail_url` points to the cited Generativ entry.

`capabilities.csv` uses the strings `true`, `false`, `unknown` to avoid silently treating an unknown as false. `source_ids` uses ` | ` separators. `sources.csv` is the complete reference table. `claim_sources.csv` uses zero-based JSON array indexes in `claim_path`; one claim can have multiple sources.

`category_summary.csv` groups systems by category. Webhook columns are mutually exclusive status counts. `tested_connections` counts entries with scoped test evidence, not all possible integrations. Every count describes this editorial sample only. No sampling weights, survey inference, popularity or adoption estimates apply.
