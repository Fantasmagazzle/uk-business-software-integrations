# UK Business Software AI Integration Database

**Can we connect AI to the software we already have?** An open, source-linked catalogue of 35 business software systems for UK integration scoping, maintained by [Generativ](https://www.generativ.co.uk/).

[Search the database](https://www.generativ.co.uk/resources/software-integration-database) · [JSON](data/integrations.json) · [CSV](data/systems.csv) · [Kaggle analysis dataset](https://www.kaggle.com/datasets/hellogenerativ/uk-business-software-ai-integration-database) · [Contribute](CONTRIBUTING.md)

## What this release covers

Accounting, CRM, productivity, work management, commerce, customer support, marketing and field service. Each entry records API style, plan restrictions, webhook/event delivery, authentication, selected read/create/update operations, limitations and official documentation.

Catalogue version: **31 October 2026**. Entry-level documentation dates range from 16 to 31 October 2026. **No scoped connection-test evidence is recorded in this dataset.** The API capability fields describe vendor documentation, not a successful connection or a promise that your tenant is entitled to it. The sample is an editorial selection for UK businesses, not a market-share study, ranking or endorsement. Many products are global; UK tax/localisation and contract details still need checking.

The ten additions include documented API shapes: base URLs, versions, request/response formats, pagination and selected endpoint summaries. Original entries without `api_contract` have not yet received this shape review. These summaries are not complete vendor OpenAPI specifications.

## Files

| File | Unit of observation / purpose |
| --- | --- |
| `data/integrations.json` | Canonical nested dataset, including citations for individual claims |
| `data/systems.csv` | One row per software system, suitable for filtering |
| `data/capabilities.csv` | One row per selected record type and its documented operations |
| `data/api_contracts.csv` | API shape overview for each reviewed system |
| `data/endpoints.csv` | Selected methods, paths, request and response shapes with source IDs |
| `data/sources.csv` | One row per official documentation source |
| `data/claim_sources.csv` | Links claims to their source IDs |
| `analysis/category_summary.csv` | Descriptive counts within this catalogue only |
| `analysis/integration_landscape.ipynb` | Reproducible exploratory analysis and charts |
| `DATA_DICTIONARY.md` | Field definitions and missing-value rules |

**Never convert `not_confirmed`, `unknown` or JSON `null` into “no”.** `conditional` means a known plan/app/contract condition applies. `event_stream` is not a generic HTTP webhook. A plan with API access does not necessarily include webhook actions, every endpoint or unlimited usage.

## Reproduce and validate

Python 3.10+; the exporter uses only the standard library. No credentials, paid APIs or vendor connections are needed.

```sh
python3 scripts/export.py
python3 -m unittest discover -s tests
```

The analysis notebook uses pandas and matplotlib (included in Kaggle). It reports counts and review gaps; it does not infer adoption, market prevalence or integration quality. For a specific project, inspect the cited endpoint, target account permissions, licence and current quota before testing.

## API for readers and LLMs

Public, read-only, no key required:

- `https://www.generativ.co.uk/api/data/software-integrations`
- `https://www.generativ.co.uk/api/data/software-integrations/xero`
- `https://www.generativ.co.uk/data/software-integrations/openapi.json`

Query the collection with `q`, `category`, `webhooks` or `verification`. Preserve the product scope, last-checked date, source IDs and test status when quoting a result. This API serves the catalogue; it does not connect to the listed products.

## Attribution and reuse

Original catalogue and analysis: **CC BY 4.0**. Code: **MIT**. Vendor documentation and trademarks remain the property of their owners; this repository links to them and does not license their content. Vendor names do not imply affiliation.

Suggested citation: Generativ (2026), *UK Business Software AI Integration Database*, version 2026-10-31, https://www.generativ.co.uk/resources/software-integration-database. Include the version or access date and identify changes when redistributing.

See [contribution instructions](CONTRIBUTING.md) to submit corrections or reproducible test evidence. Updates are reviewed; this is a dated snapshot, not a real-time vendor status feed.

## Discovery backlog

Zapier and n8n connector directories help identify additional candidates. A listing does not establish direct API entitlement, endpoint coverage or a tested connection. See [the sourced expansion backlog](EXPANSION_BACKLOG.md); each candidate needs its own official vendor documentation review before entering the main dataset.
