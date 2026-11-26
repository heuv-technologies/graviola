# Connect Graviola to Gemini CLI for professional people search

Graviola is a product of Heuv Technologies. Its hosted MCP server provides professional people search, available contact data, projects and authorized email workflows. The public repository contains connection configuration, documentation and examples; it does not contain the hosted server implementation.

## Requirements

- A current Gemini CLI installation and its normal model authentication.
- A Graviola account with access to the workspace you want to use.
- A local browser that can complete OAuth and return to a localhost callback.

Graviola plan allowances and your Gemini service terms are separate. This guide does not assert that all Gemini CLI versions have been tested with Graviola. The public manifest and the commands below follow the current Gemini CLI documentation; a complete Gemini sign-in and tool execution test has not been performed in this publication.

## Install the connection extension

Review [gemini-extension.json](../gemini-extension.json), then run:

```sh
gemini extensions install https://github.com/heuv-technologies/graviola
```

Review the CLI's installation prompt. The manifest points directly to `https://mcp.graviola.dev/api/mcp` using Streamable HTTP. It contains no API key or local executable. `trust` is `false`; installing this extension does not automatically approve tool calls.

If you already configured a server named `graviola` in Gemini CLI settings, review that configuration first: a settings entry with the same name takes precedence over an extension entry.

## Authenticate with your own Graviola account

Open Gemini CLI and use:

```text
/mcp
/mcp auth graviola
```

Complete the browser sign-in and review the workspace and access level in Graviola's consent screen. OAuth discovery is handled by the client. Do not paste an access token into an issue, chat, extension manifest or public configuration.

If the CLI reports a failed callback, check that its local browser can receive the localhost redirect. Gemini's OAuth documentation describes limitations in headless, container and remote SSH environments. Preserve issuer validation and other authentication checks when diagnosing a failure.

## Start with workspace information

Before spending search or contact credits, try:

```text
Show my Graviola workspace, available allowances and accessible projects.
Do not search for people, reveal contact details or send messages.
```

Review the actual result and the workspace identity. An installed manifest is not proof that authentication or data access succeeded.

## Prepare a narrow people search

For example, ask for a proposed search for founding engineers with Rust and PostgreSQL experience:

```text
Prepare a Graviola search for at most five potential founding backend
engineers in [location], using supported role and skill filters for Rust
and PostgreSQL. Show the proposed filters, expected credit use and the
evidence we would need to review. Do not execute the search yet.
```

When the proposal matches your brief, authorize the search separately. Review professional evidence before saving a shortlist or requesting available contact data. A skill match does not establish willingness to change jobs, current availability or suitability for a hiring decision.

For a complete sourcing workflow, use the [Rust and PostgreSQL founding engineer tutorial](https://graviola.dev/blog/find-founding-rust-postgresql-engineers). For editorial research, use the [usage-based SaaS podcast guest workflow](https://graviola.dev/blog/find-podcast-guests-usage-based-pricing).

## Troubleshooting

- **No Graviola entry:** check that the extension was installed and the manifest is present at the repository root.
- **An unexpected endpoint:** check for a settings entry that overrides the extension's `graviola` alias.
- **Authentication required:** use `/mcp auth graviola` and finish the browser flow.
- **No access to the intended project:** review the selected workspace, role and project visibility.
- **Insufficient credits or unavailable contacts:** check Graviola's current allowances and the returned availability information; reconnecting does not increase either.

Include the client version and a redacted error when reporting a connection problem. Never include credentials, candidate records or mailbox contents. Contact Toni at [toni@graviola.dev](mailto:toni@graviola.dev).

## References

- [Gemini CLI extension reference](https://geminicli.com/docs/extensions/reference/)
- [Gemini CLI MCP and OAuth documentation](https://geminicli.com/docs/tools/mcp-server/)
- [Graviola connection documentation](https://graviola.dev/docs/connect-your-ai)
- [Current Graviola product facts and limits](https://graviola.dev/product)

Reviewed November 26, 2026. Gallery inclusion, search-engine indexation and client sign-in are separate states.
