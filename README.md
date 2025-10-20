# 🧠 Gemma3 Smart Q4

**Bilingual offline AI assistant optimized for Raspberry Pi**

This repository contains code, demos, and instructions for using **Gemma3 Smart Q4**, a quantized Gemma 3 1B model that runs completely offline on Raspberry Pi 4/5.

---

## 🔗 Download the Model

**Hugging Face**: [chill123/gemma3-smart-q4](https://huggingface.co/chill123/gemma3-smart-q4)

Two versions available:
- **Q4_0** (687 MB) ⭐ **Recommended** - Faster speed, ~3.67 tokens/s
- **Q4_K_M** (769 MB) - Better quality, ~3.56 tokens/s

---

## 🚀 Quick Start

```bash
# Option 1: Pull from Hugging Face
cat > Modelfile <<'MODELFILE'
FROM hf.co/chill123/gemma3-smart-q4/gemma3-1b-q4_0.gguf

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_ctx 1024
PARAMETER num_thread 4
PARAMETER num_batch 32
PARAMETER repeat_penalty 1.05

SYSTEM """
You are an offline AI assistant on Raspberry Pi. Detect user language (IT/EN) and respond accordingly.
Sei un assistente AI offline su Raspberry Pi. Rileva la lingua (IT/EN) e rispondi di conseguenza.
"""
MODELFILE

ollama create gemma3-smart-q4 -f Modelfile
ollama run gemma3-smart-q4 "Hello! Who are you?"
```

---

## 📂 Demo Scripts

### Bash Test Script

See [demo/ollama_test.sh](demo/ollama_test.sh)

```bash
chmod +x demo/ollama_test.sh
./demo/ollama_test.sh gemma3-smart-q4 "Ciao! Presentati."
```

### Python API Test

See [demo/ollama_api_test.py](demo/ollama_api_test.py)

```bash
python3 demo/ollama_api_test.py gemma3-smart-q4 "Explain what a Raspberry Pi is."
```

---

## 🎯 Features

- ✅ **Fully offline** — No internet required
- ✅ **Bilingual** — Italian and English support
- ✅ **Privacy-first** — All data stays on your device
- ✅ **Fast** — 3.56-3.67 tokens/s on Raspberry Pi 4
- ✅ **Lightweight** — Under 800 MB

---

## 📊 Benchmark Results

Tested on Raspberry Pi 4 (4GB):

| Model | Speed | File Size | Use Case |
|-------|-------|-----------|----------|
| Q4_0 ⭐ | **3.67 t/s** | 687 MB | **Default choice** |
| Q4_K_M | 3.56 t/s | 769 MB | Extended conversations |

**Individual test results**:
- Q4_0: 3.65, 3.67, 3.70 tokens/s
- Q4_K_M: 3.71, 3.58, 3.40 tokens/s

---

## 🔖 License

Derivative work of [Google Gemma 3 1B](https://huggingface.co/google/gemma-3-1b-it).
See [Gemma License](https://ai.google.dev/gemma/terms).

**Quantization and optimization by Antonio (chill123).**

---

**Built with ❤️ by Antonio 🇮🇹**
