# People search and email outreach with your own AI

Graviola provides available professional data, saved contacts and email operations. Your assistant interprets the brief, evaluates the evidence and writes the message. This guide separates those responsibilities so you can inspect the result at each step.

These are example requests, not customer results or a promise of contact coverage. The route names and authentication metadata were checked against the public API on November 25, 2026. A full search-and-send run is not claimed here.

## Connect and inspect your workspace

Follow the [connection guide](connect.md). Graviola's remote MCP endpoint is:

```text
https://mcp.graviola.dev/api/mcp
```

Use your client's OAuth flow. Availability in a client's public directory is separate from support for connecting a remote MCP server.

Start with a read-only request:

```text
Show the account and workspace connected to Graviola, remaining allowances,
and the available workflow tools. Do not run external searches, reveal
contact details, create records or send messages.
```

Check that the connected account and workspace are the ones you intended. Do not substitute another account if the intended one is disconnected.

## Turn a brief into explicit search criteria

```text
Help me define a search for engineering leaders at developer tools
companies in the United States. Separate requirements we can search
directly from facts you need to verify after retrieving profiles.
Show the proposed query and filters before running a search.
```

The assistant should state what is supported and what is unknown. A discovery result is not yet an evidenced match. For example, a title alone does not prove a person's buying authority or interest.

## Search once and assess the evidence

```text
Use at most one new Graviola people search for the criteria we agreed.
Review up to five returned profiles. Explain each match using available
work history and company evidence. Mark missing facts as unknown.
Do not reveal contacts or send email. Return the saved search ID.
```

Search allowance applies even when useful matches are sparse. When reviewing a saved search, use the existing results rather than repeating the external search. Profile loading can be incomplete; inspect its status and report partial results.

## Reveal only selected contacts

```text
For the profiles I selected, preview the available contact action and
current allowance. After I request the reveal, use at most two work-email
reveals. Preserve the returned status and source. Do not invent missing
addresses or interpret an unknown status as verified.
```

An available address does not guarantee that a message will arrive, that the person is interested, or that outreach is appropriate. Use the [current plans and limits](https://graviola.dev/docs/credits-and-plans).

## Prepare a bounded email sequence

```text
Draft one short first email using only the evidence we reviewed.
Show the recipient, sender mailbox, exact text, timezone, schedule,
follow-up steps and applicable sending limits. Do not send or queue
anything until I request that exact action.
```

Sending requires an authorized connected mailbox, the applicable paid plan and sufficient capacity. Access settings may require review in Graviola. Inspect the returned state after scheduling; a queued message is not yet a message accepted by the provider.

## Follow the conversation

```text
Read recorded replies for this sequence and show the matching original
conversation when available. Distinguish accepted messages, delivery
reports and replies. Draft a response for me to review. Do not send it.
```

Provider support and accessible message history differ by mailbox. A missing reply is not proof that no reply exists outside the captured history. Confirm the recorded follow-up state after a reply instead of assuming every pending action has stopped.

## Build the same workflow with the API

Use a private workspace API key in a server environment. The [read-only Python example](../examples/workspace_readonly.py) first checks workspace identity and then reads allowances. It does not search, reveal or send.

The [live OpenAPI specification](https://api.graviola.dev/api/v1/openapi.json) is the reference for request schemas. Do not paste keys into chat, commit them to GitHub or put them in browser code. For an uncertain write, inspect the recorded state before retrying and follow the operation's request-ID rules.

## Useful references

- [Graviola product and availability](https://graviola.dev/product)
- [Search and profile evidence](https://graviola.dev/docs/review-profiles)
- [Email sequences and limits](https://graviola.dev/docs/email-sequences)
- [Authentication and troubleshooting](https://graviola.dev/docs/troubleshooting)

This repository documents the hosted service. It does not include the product's private implementation or client data.
