#!/usr/bin/env bash
# Quick test script for Ollama models

set -euo pipefail

MODEL="${1:-gemma3-smart-q4}"
PROMPT="${2:-Ciao! Presentati in una frase.}"

echo "╔════════════════════════════════════════╗"
echo "║      Ollama Model Test                 ║"
echo "╚════════════════════════════════════════╝"
echo ""
echo "Model:  $MODEL"
echo "Prompt: $PROMPT"
echo ""
echo "Response:"
echo "----------------------------------------"

ollama run "$MODEL" "$PROMPT"

echo ""
echo "✅ Test complete"
