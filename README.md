<p align="center"><a href="https://graviola.dev"><img src="https://graviola.dev/graviola-mcp.png" width="80" alt="Graviola"></a></p>

# Graviola

Find your next hire. Meet your next customer.

Graviola is a product of **Heuv Technologies**. Contact: **Toni** — [toni@graviola.dev](mailto:toni@graviola.dev).

People search, available contact data and email outreach infrastructure for your own AI. Your assistant plans, evaluates professional evidence and writes; Graviola retrieves data, organizes contacts and runs authorized workflows.

[Website](https://graviola.dev) · [Create an account](https://data.graviola.dev/signup) · [Connect your AI](https://data.graviola.dev/#developer) · [Product guide](https://graviola.dev/product)

## Connect Claude Code

```sh
claude mcp add --transport http --scope user graviola https://mcp.graviola.dev/api/mcp
```

Open Claude Code, run `/mcp`, select Graviola and sign in. Choose your workspace and access level.

Start with:

```text
Show my Graviola workspace, available credits and projects.
Do not run searches or send emails yet.
```

[Connection guide](docs/connect.md) · [MCP connection diagnostics](docs/mcp-authentication-diagnostics.md) · [Workflow prompts](docs/workflows.md) · [REST API example](examples/usage.sh) · [People data and outreach tutorial](docs/people-data-for-your-ai.md) · [Python workspace example](examples/workspace_readonly.py)

## What you can build

| Recruiting | Sales |
| :--- | :--- |
| Find candidates by role, location, skills and education | Find prospects by professional profile and company |
| Review available experience and education | Review relevant background before contacting |
| Save candidates to projects and shortlists | Organize prospects and export CSV |
| Personalize email sequences and follow-ups | Run scheduled outreach from connected mailboxes |

Use Claude, Claude Code, Codex, Cursor or another compatible MCP client. Connect Gmail or Microsoft 365 for email and HubSpot for contact sync.

## Endpoints

| Interface | URL |
| :--- | :--- |
| MCP, Streamable HTTP | `https://mcp.graviola.dev/api/mcp` |
| REST API | `https://api.graviola.dev/api/v1` |
| Product facts for agents | [llms.txt](https://graviola.dev/llms.txt) |
| Structured product manifest | [graviola.json](https://graviola.dev/.well-known/graviola.json) |

Protected operations require authentication. Available fields, credits, permissions, mailbox limits and applicable approvals govern execution. Contact details and hiring or sales outcomes are not guaranteed.


## Workflow guides

Practical guides on the Graviola website:

- [Find VC investor contacts with your own AI](https://graviola.dev/blog/find-vc-investor-contacts-with-ai)
- [Find podcast guests and prepare outreach](https://graviola.dev/blog/podcast-guest-outreach-with-ai)
- [Find early customers with AI-assisted prospecting](https://graviola.dev/blog/first-customers-outbound-with-ai)

- [People search MCP tutorial](https://graviola.dev/blog/people-search-mcp-tutorial)
- [People search REST API workflow](https://graviola.dev/blog/people-search-api-workflow)
- [Contact enrichment and work email statuses](https://graviola.dev/blog/contact-enrichment-work-email-guide)
- [Email sequence preparation and reply review](https://graviola.dev/blog/ai-email-sequence-tutorial)
- [AI recruiting sourcing walkthrough](https://graviola.dev/blog/ai-recruiting-sourcing-shortlist)
- [Evaluate contact data providers with a consistent sample](https://graviola.dev/blog/compare-b2b-contact-data-providers)

### Specific use cases

- [Find founding engineers with Rust and PostgreSQL experience](https://graviola.dev/blog/find-founding-rust-postgresql-engineers)
- [Find payroll API partnership leaders for HRIS integrations](https://graviola.dev/blog/find-payroll-api-partnership-leaders)
- [Find podcast guests with usage-based SaaS pricing experience](https://graviola.dev/blog/find-podcast-guests-usage-based-pricing)
- [Research RevOps contacts for a HubSpot-to-Salesforce migration offer](https://graviola.dev/blog/find-revops-leaders-hubspot-salesforce-migration)
- [Find DevRel speakers for a RAG evaluation workshop](https://graviola.dev/blog/find-developer-relations-speakers-rag-evaluation)
- [Find participants for B2B onboarding research](https://graviola.dev/blog/find-customer-interview-participants-b2b-onboarding)

## Guias em português

- [Encontrar convidados de podcast sobre precificação por uso em SaaS](https://graviola.dev/blog/como-encontrar-convidados-podcast-precificacao-por-uso-saas)
- [Guia no site: líderes de RevOps para migração HubSpot–Salesforce](https://graviola.dev/blog/como-encontrar-revops-migracao-hubspot-salesforce)

- [Encontrar líderes de RevOps para uma oferta de migração HubSpot–Salesforce](docs/pt-br/encontrar-revops-migracao-hubspot-salesforce.md)

- [Buscar candidatos com sua própria IA via MCP](docs/pt-br/buscar-candidatos-com-ia-mcp.md)
- [Pesquisar contatos de investidores e convidados de podcasts](docs/pt-br/pesquisar-investidores-e-podcasts.md)
- [Prospectar os primeiros clientes B2B com sua própria IA](docs/pt-br/prospectar-clientes-com-ia.md)

## Compare workflows

[Graviola comparisons](https://graviola.dev/compare) cover professional search, contact data, recruiting and email outreach products. Each new comparison links official product information and proposes a practical evaluation. Recommendations are editorial assessments, not measured vendor rankings.

## Public directory listings

- [Official MCP Registry](https://registry.modelcontextprotocol.io/?q=io.github.heuv-technologies%2Fgraviola)
- [Graviola on Glama — Heuv Technologies](https://glama.ai/mcp/connectors/io.github.heuv-technologies/graviola)
- [Graviola on Product Hunt](https://www.producthunt.com/products/graviola)
- [Graviola on Gate of AI](https://gateofai.com/community-tools/graviola/)
- [Graviola on Indie Hackers](https://www.indiehackers.com/product/graviola)

## About this repository

Public connection guides and examples for Graviola. This repository does not contain the hosted product source code. For account support, use the Graviola app. Never post API keys, candidate records or mailbox contents in GitHub issues.


