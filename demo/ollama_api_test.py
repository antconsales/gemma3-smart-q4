#!/usr/bin/env python3
"""
Ollama API Test Script
Tests model inference via HTTP API (no external dependencies)
"""

import json
import sys
import urllib.request

def test_ollama(model="gemma3-smart-q4", prompt="Explain what a Raspberry Pi is in one sentence."):
    """Test Ollama model via HTTP API"""

    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    print("╔════════════════════════════════════════╗")
    print("║      Ollama API Test                   ║")
    print("╚════════════════════════════════════════╝")
    print(f"\nModel:  {model}")
    print(f"Prompt: {prompt}\n")
    print("Response:")
    print("-" * 40)

    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            response_text = result.get("response", "<no response>")
            print(response_text)

            # Optional: print metrics
            if result.get("eval_count") and result.get("eval_duration"):
                tokens = result["eval_count"]
                duration_ns = result["eval_duration"]
                tokens_per_sec = tokens / (duration_ns / 1e9)
                print(f"\n\n📊 Speed: {tokens_per_sec:.2f} tokens/s")

        print("\n✅ Test complete")

    except urllib.error.URLError as e:
        print(f"\n❌ Error: {e}")
        print("Make sure Ollama is running: ollama serve")
        sys.exit(1)

if __name__ == "__main__":
    model = sys.argv[1] if len(sys.argv) > 1 else "gemma3-smart-q4"
    prompt = sys.argv[2] if len(sys.argv) > 2 else "Explain what a Raspberry Pi is in one sentence."
    test_ollama(model, prompt)
