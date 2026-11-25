# Diagnose a remote Graviola MCP connection

Graviola is a hosted Streamable HTTP MCP service. The endpoint is not a web page. Opening it in a browser and seeing an error is different from an authenticated MCP client failing to connect.

This walkthrough records public, unauthenticated checks performed on November 25, 2026. No workspace data, paid searches, contact reveals or email sends were involved. It does not establish that an authenticated end-to-end workflow works in every client.

## Check OAuth discovery

```sh
curl --fail --silent --show-error \
  https://mcp.graviola.dev/.well-known/oauth-authorization-server
```

The observed JSON identified these endpoints:

| Field | Observed value |
| :--- | :--- |
| issuer | `https://mcp.graviola.dev` |
| authorization_endpoint | `https://mcp.graviola.dev/mcp/connect` |
| token_endpoint | `https://mcp.graviola.dev/api/mcp/oauth/token` |
| registration_endpoint | `https://mcp.graviola.dev/api/mcp/oauth/register` |
| response_types_supported | `code` |
| code_challenge_methods_supported | `S256` |

Your MCP client should perform its supported authorization flow. A successful dynamic client registration is not the same as a user authorizing access to a workspace.

## Check the anonymous MCP response

The following request initializes a connection without credentials. It deliberately does not call a business tool:

```sh
curl --silent --show-error --include \
  https://mcp.graviola.dev/api/mcp \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json, text/event-stream' \
  --data '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"graviola-discovery-check","version":"1.0.0"}}}'
```

The observed response was HTTP `401`, with a JSON-RPC error:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32001,
    "message": "Connect your verified Graviola account using OAuth."
  }
}
```

This confirms that the public endpoint answered and required authentication for this request. It does not prove that a credential is valid or that a particular plan includes an action. Use your client's OAuth connection screen to continue, then inspect your account, workspace and allowances.

## Why a browser visit can return 405

An anonymous GET request to the same endpoint returned HTTP `405` and `Allow: POST, OPTIONS` during the check. Do not use a successful HTML page load as the health criterion for this MCP endpoint. Check the protocol request and authentication state instead.

## If a directory labels the connector unhealthy

An anonymous health check may stop at authentication. First determine whether the directory supports OAuth and whether it requires a dedicated test profile. Do not weaken production authentication merely to change a directory badge.

Never provide a directory with a live customer workspace credential. If a test account is required, use an isolated account with the minimum access; review the directory's requested access and health-check behavior before authorizing it. Never put credentials in a public issue or listing.

## What to share in a support report

Share the client name and version, public endpoint, HTTP status, and a redacted error message. Keep API keys, OAuth codes, session cookies, contact records and mailbox contents private. A timeout is an uncertain result, not proof that an operation did or did not execute.

[Connection guide](connect.md) · [Workflow walkthrough](people-data-for-your-ai.md) · [Graviola troubleshooting](https://graviola.dev/docs/troubleshooting)
