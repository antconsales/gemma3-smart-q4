# 🧠 Gemma3 Smart Q4 — Bilingual Offline Assistant for Raspberry Pi

**Bilingual offline AI assistant optimized for Raspberry Pi**

This repository contains code, demos, benchmark scripts, and instructions for **Gemma3 Smart Q4**, a quantized bilingual (Italian–English) variant of Google's Gemma 3 1B model, specifically optimized for edge devices like the **Raspberry Pi 4 & 5**.

**Version**: v0.1.0
**Author**: Antonio ([chill123](https://huggingface.co/chill123))
**Base Model**: [Google Gemma 3 1B IT](https://huggingface.co/google/gemma-3-1b-it)

---

## 🔗 Download the Model

**Ollama** 🚀 (Recommended): [antconsales/antonio-gemma3-smart-q4](https://ollama.com/antconsales/antonio-gemma3-smart-q4)
```bash
ollama pull antconsales/antonio-gemma3-smart-q4
```

**Hugging Face**: [chill123/antonio-gemma3-smart-q4](https://huggingface.co/chill123/antonio-gemma3-smart-q4)

Two versions available:
- **Q4_0** (687 MB) ⭐ **Recommended** - Faster speed, ~3.67 tokens/s
- **Q4_K_M** (769 MB) - Better quality, ~3.56 tokens/s

---

## 🚀 Quick Start

**⚠️ IMPORTANT**: To enable bilingual behavior, you **must** create a Modelfile with the bilingual SYSTEM prompt (shown below). Simply running `ollama pull` without the Modelfile will result in English-only responses.

### Option 1: Use Published Ollama Model (Recommended)

```bash
# Step 1: Pull the model
ollama pull antconsales/antonio-gemma3-smart-q4

# Step 2: Create Modelfile with bilingual configuration
cat > Modelfile <<'MODELFILE'
FROM antconsales/antonio-gemma3-smart-q4

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_ctx 1024
PARAMETER num_thread 4
PARAMETER num_batch 32
PARAMETER repeat_penalty 1.05
PARAMETER stop "<end_of_turn>"
PARAMETER stop "</s>"

SYSTEM """You are an offline AI assistant running on a Raspberry Pi. You MUST detect the user's language and respond in the SAME language:

- If the user writes in Italian, respond ONLY in Italian
- If the user writes in English, respond ONLY in English

Sei un assistente AI offline su Raspberry Pi. DEVI rilevare la lingua dell'utente e rispondere nella STESSA lingua:

- Se l'utente scrive in italiano, rispondi SOLO in italiano
- Se l'utente scrive in inglese, rispondi SOLO in inglese

Always match the user's language choice."""
MODELFILE

# Step 3: Create configured model
ollama create gemma3-bilingual -f Modelfile

# Step 4: Test it!
ollama run gemma3-bilingual "Ciao! Come stai?"
ollama run gemma3-bilingual "Hello! How are you?"
```

### Option 2: Pull Directly from Hugging Face

```bash
cat > Modelfile <<'MODELFILE'
FROM hf://chill123/antonio-gemma3-smart-q4/gemma3-1b-q4_0.gguf

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_ctx 1024
PARAMETER num_thread 4
PARAMETER num_batch 32
PARAMETER repeat_penalty 1.05
PARAMETER stop "<end_of_turn>"
PARAMETER stop "</s>"

SYSTEM """You are an offline AI assistant. Detect user language (Italian/English) and respond in the same language.

Sei un assistente AI offline. Rileva la lingua dell'utente (italiano/inglese) e rispondi nella stessa lingua."""
MODELFILE

ollama create gemma3-bilingual -f Modelfile
ollama run gemma3-bilingual
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

### Benchmark Methodology

Benchmark executed on **Raspberry Pi 4 (4GB)** using 3 bilingual prompts (mixed Italian/English).
Average eval rate calculated from `eval rate:` logs only, excluding load and warm-up time.
Runtime: Ollama 0.x on Raspberry Pi OS (Debian Bookworm).

> **Recommendation**: Use **Q4_0** as default (3% faster, 82MB smaller, equivalent quality). Use **Q4_K_M** only if you need slightly better coherence in very long conversations (1000+ tokens).

---

## ⚙️ Recommended Settings (Raspberry Pi 4)

For **optimal performance** on Raspberry Pi 4/5, use these parameters:

| Parameter | Value | Description |
|-----------|-------|-------------|
| `num_ctx` | `512` - `1024` | Context length (512 for faster response, 1024 for longer conversations) |
| `num_thread` | `4` | Utilize all 4 cores on Raspberry Pi 4 |
| `num_batch` | `32` | Optimized for throughput on Pi |
| `temperature` | `0.7` - `0.8` | Balanced creativity vs consistency |
| `top_p` | `0.9` | Nucleus sampling for diverse responses |
| `repeat_penalty` | `1.05` | Reduces repetitive outputs |

**For voice assistants** or **real-time chat**, reduce `num_ctx` to `512` for faster responses.

---

## 💬 Try These Prompts

Test the bilingual capabilities with these examples:

### 🇮🇹 Italian

```bash
ollama run gemma3-smart-q4 "Spiegami la differenza tra sensore IR e ultrasuoni in due frasi."
```

```bash
ollama run gemma3-smart-q4 "Come posso controllare un LED con GPIO su Raspberry Pi?"
```

### 🇬🇧 English

```bash
ollama run gemma3-smart-q4 "Outline a 5-step plan to control a servo with GPIO on Raspberry Pi."
```

```bash
ollama run gemma3-smart-q4 "What are the best uses for a Raspberry Pi in home automation?"
```

### 🌍 Code-switching

```bash
ollama run gemma3-smart-q4 "Explain in English how to install Ollama, poi spiega in italiano come testare il modello."
```

---

## 🔒 Model Verification

Verify downloaded models using SHA256 checksums:

| File | SHA256 Checksum |
|------|----------------|
| `gemma3-1b-q4_0.gguf` | `d1d037446a2836db7666aa6ced3ce460b0f7f2ba61c816494a098bb816f2ad55` |
| `gemma3-1b-q4_k_m.gguf` | `c02d2e6f68fd34e9e66dff6a31d3f95fccb6db51f2be0b51f26136a85f7ec1f0` |

```bash
# Verify checksum on Linux/Mac
sha256sum gemma3-1b-q4_0.gguf
```

---

## 🔖 License

This model is a **derivative work** of [Google's Gemma 3 1B](https://huggingface.co/google/gemma-3-1b-it).

**License**: Gemma License
Please review and comply with the [Gemma License Terms](https://ai.google.dev/gemma/terms) before using this model.

**Quantization, optimization, and bilingual configuration** by Antonio (chill123).

For licensing questions regarding the base model, refer to Google's official Gemma documentation.

---

## 🛠️ Technical Details

**Base Model**: Google Gemma 3 1B (instruction-tuned)
**Quantization**: Q4_0 and Q4_K_M (llama.cpp)
**Context Length**: 1024 tokens (configurable)
**Vocabulary Size**: 262,144 tokens
**Architecture**: Gemma3ForCausalLM
**Supported Platforms**: Raspberry Pi 4/5, Mac M1/M2, Linux ARM64

---

## 📝 Version History

### v0.1.0 (2025-10-21)
- Initial release
- Two quantizations: Q4_0 (687 MB) and Q4_K_M (769 MB)
- Bilingual IT/EN support with automatic language detection
- Optimized for Raspberry Pi 4 (3.56-3.67 tokens/s)
- Tested on Raspberry Pi OS (Debian Bookworm) with Ollama

---

**Built with ❤️ by Antonio 🇮🇹**
*Empowering privacy and edge computing, one model at a time.*
