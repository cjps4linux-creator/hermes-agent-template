#!/usr/bin/env bash
set -euo pipefail
if [ $# -lt 1 ]; then
  echo "usage: skeleton.sh <agent-name> [owner]"
  exit 1
fi
NAME="$1"
OWNER="${2:-unknown}"
DEST="agents/${NAME}"
mkdir -p "${DEST}"
sed -e "s/{AGENT_NAME}/${NAME}/g" -e "s/{OWNER}/${OWNER}/g" \
  agent/AGENT.md > "${DEST}/SOUL.md"
cp agent/agent.spec.md "${DEST}/contract.md"
echo "created: ${DEST}/SOUL.md"
echo "created: ${DEST}/contract.md"
