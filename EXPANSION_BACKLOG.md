# Platforms to investigate next

Discovery reviewed 16 October 2026. These are **research candidates, not entries in the verified documentation catalogue**. Connector listings help identify useful systems but do not prove a public API, a particular subscription entitlement or a tested connection. Before adding a row, follow CONTRIBUTING.md and cite the vendor's own documentation.

| Candidate | Discovery source | Why investigate | Evidence still needed |
| --- | --- | --- | --- |
| ServiceM8 | [Zapier listing](https://zapier.com/apps/servicem8/integrations) | Job management for service businesses | Vendor API, plan, auth, job/customer operations and webhook limits |
| Simpro | [Zapier listing with ServiceM8](https://zapier.com/apps/servicem8/integrations/simpro) | Field service and trade workflows | Vendor API entitlement, object coverage, auth and event delivery |
| Capsule CRM | [n8n integration page](https://n8n.io/integrations/capsule/) and [Zapier listing](https://zapier.com/apps/capsulecrm/integrations/servicem8) | Contact and opportunity workflows | Vendor plan/access rules and endpoint evidence; n8n's page describes the generic HTTP Request node, not a dedicated built-in Capsule node |
| BambooHR | [n8n integration page](https://n8n.io/integrations/bamboohr/) | Adds an HR category absent from the starter set | Vendor licence, permissions, field restrictions and webhook rules |
| ERPNext | [n8n integration page](https://n8n.io/integrations/erpnext/) | Adds an open-source ERP option | Hosting/version scope, vendor authentication, document permissions and event configuration |

## Discovery method

Use the [Zapier directory](https://zapier.com/apps) and [n8n directory](https://n8n.io/integrations/) to find platform names and possible workflows. Distinguish dedicated nodes, community nodes, generic HTTP recipes and third-party connectors. Check whether a trigger is polling or event-driven. Do not copy marketing endpoint lists into the main dataset without checking official vendor references. No connector has been installed or tested as part of this discovery.
