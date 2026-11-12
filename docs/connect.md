# Connect Graviola

## Claude Code

1. Install Claude Code using its [official instructions](https://code.claude.com/docs/en/overview).
2. Register Graviola:

   ```sh
   claude mcp add --transport http --scope user graviola https://mcp.graviola.dev/api/mcp
   ```

3. Open Claude Code and run `/mcp`.
4. Select Graviola, sign in and choose your workspace permissions.
5. Ask it to show your workspace and remaining credits.

OAuth handles sign-in. You do not need to paste an API key into your conversation.

## Other MCP clients

Add a remote Streamable HTTP server with this URL:

```text
https://mcp.graviola.dev/api/mcp
```

Use the client's OAuth sign-in flow when supported. Client capabilities and subscription requirements vary. See the [Graviola connection screen](https://data.graviola.dev/#developer) for client-specific setup prompts.

## REST API

Create a workspace API key in the Graviola app. Keep it in your local environment or secret manager. Send it as a Bearer token.

```sh
bash examples/usage.sh
```

The example requires `GRAVIOLA_API_KEY` to be set and only reads usage. Authenticated route schemas are available at `https://api.graviola.dev/api/v1/openapi.json`.

## Troubleshooting

| Issue | Check |
| :--- | :--- |
| Sign-in required | Reconnect through your client's MCP settings |
| Permission denied | Workspace membership and granted access |
| Search or reveal unavailable | Current plan and remaining credits |
| Email cannot send | Connected mailbox, paid outreach allowance and sending limits |
| Approval requested | Complete the applicable authorization in Graviola |

[Claude Code MCP documentation](https://code.claude.com/docs/en/mcp)
