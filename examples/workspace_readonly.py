#!/usr/bin/env python3
"""Read workspace identity and usage. No searches, reveals, or sends."""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

BASE_URL = "https://api.graviola.dev/api/v1"


def read_action(action, payload, key):
    request = urllib.request.Request(
        f"{BASE_URL}/actions/{action}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        # Do not echo arbitrary response bodies or credentials to a terminal log.
        raise RuntimeError(f"{action}: HTTP {error.code}; check access and the live API documentation") from None
    except (urllib.error.URLError, TimeoutError):
        raise RuntimeError(f"{action}: connection failed; no automatic retry was performed") from None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-id", help="Optional workspace ID; OAuth connections remain bound to their approved workspace")
    parser.add_argument("--usage", action="store_true", help="Read allowances after you have checked workspace identity in a previous invocation")
    args = parser.parse_args()
    key = os.environ.get("GRAVIOLA_API_KEY", "").strip()
    if not key:
        parser.error("Set GRAVIOLA_API_KEY in your private environment")
    payload = {"workspaceId": args.workspace_id} if args.workspace_id else {}
    action = "usage_get" if args.usage else "workspace_status"
    try:
        result = read_action(action, payload, key)
    except (RuntimeError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
