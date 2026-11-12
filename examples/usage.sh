#!/usr/bin/env bash
set -euo pipefail
: "${GRAVIOLA_API_KEY:?Set GRAVIOLA_API_KEY in your environment}"
curl --fail-with-body --silent --show-error \
  --header "Authorization: Bearer ${GRAVIOLA_API_KEY}" \
  --header 'Accept: application/json' \
  'https://api.graviola.dev/api/v1/usage'
