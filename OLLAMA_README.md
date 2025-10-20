# Gemma3 Smart Q4 — Bilingual Offline AI for Raspberry Pi

**Quantized Gemma 3 1B optimized for edge devices. Fully offline, bilingual (Italian/English), privacy-first.**

---

## 🚀 Quick Start

**IMPORTANT**: To enable bilingual behavior, you must create a Modelfile with the bilingual SYSTEM prompt.

### Step 1: Pull the base model

```bash
# Pull Q4_0 (recommended - faster, smaller)
ollama pull antconsales/antonio-gemma3-smart-q4

# Or pull Q4_K_M variant (better quality for long conversations)
ollama pull antconsales/antonio-gemma3-smart-q4:q4_k_m
```

### Step 2: Create Modelfile with bilingual configuration

```bash
cat > Modelfile <<'EOF'
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
EOF
```

### Step 3: Create the configured model

```bash
ollama create gemma3-bilingual -f Modelfile
```

### Step 4: Run it!

```bash
ollama run gemma3-bilingual

# Test in Italian
>>> ciao! come va?

# Test in English
>>> hello! how are you?
```

**Why this is needed**: The base model is instruction-tuned but doesn't automatically switch languages. The SYSTEM prompt explicitly tells it to match the user's language.

## ✨ Features

- 🔒 **100% Offline** — No cloud, no tracking, no internet required
- 🗣️ **Bilingual** — Automatically detects and responds in Italian or English
- ⚡ **Fast** — 3.67 tokens/s on Raspberry Pi 4 (Q4_0)
- 🎯 **Optimized** — Tuned parameters for Pi 4/5 hardware
- 🔐 **Privacy-First** — All inference on-device

## 📊 Benchmarks (Raspberry Pi 4, 4GB RAM)

| Model | Speed | Size | Use Case |
|-------|-------|------|----------|
| **Q4_0** ⭐ | **3.67 t/s** | 720 MB | Default choice (faster, smaller) |
| **Q4_K_M** | 3.56 t/s | 806 MB | Better coherence in long conversations |

**Tested on**: Raspberry Pi OS (Debian Bookworm), Ollama runtime

## 💬 Example Interactions

Once you've created the model with the Modelfile (see Quick Start above):

### Italian
```bash
ollama run gemma3-bilingual "Ciao! Spiegami cos'è un sensore di prossimità."
```

### English
```bash
ollama run gemma3-bilingual "What is a Raspberry Pi and what can I do with it?"
```

### Code-switching (IT/EN mixed)
```bash
ollama run gemma3-bilingual "Explain GPIO in English, poi dimmi come usarlo in italiano"
```

The model automatically detects the language and responds appropriately **when using the Modelfile configuration**!

## 🎯 Use Cases

- **Privacy-first personal assistants** — All inference on-device
- **Offline home automation** — Control IoT without cloud dependencies
- **Voice assistants** — Fast enough for real-time speech (3.67 t/s)
- **Educational Pi projects** — Learn AI/ML on affordable hardware
- **Bilingual chatbots** — IT/EN customer support, documentation
- **Embedded systems** — Industrial applications requiring offline inference

## ⚙️ Recommended Settings (Raspberry Pi 4/5)

For **optimal performance**, use these parameters in your Modelfile:

```dockerfile
FROM antconsales/antonio-gemma3-smart-q4

PARAMETER num_ctx 1024       # Context length (512 for faster response, 1024 for longer conversations)
PARAMETER num_thread 4        # Utilize all 4 cores on Raspberry Pi 4
PARAMETER num_batch 32        # Optimized for throughput on Pi
PARAMETER temperature 0.7     # Balanced creativity vs consistency
PARAMETER top_p 0.9           # Nucleus sampling for diverse responses
PARAMETER repeat_penalty 1.05 # Reduces repetitive outputs
PARAMETER stop "<end_of_turn>"
PARAMETER stop "</s>"

SYSTEM """
You are an offline AI assistant running on a Raspberry Pi. Automatically detect the user's language (Italian or English) and respond in the same language. Be concise, practical, and helpful.

Sei un assistente AI offline che opera su Raspberry Pi. Rileva automaticamente la lingua dell'utente (italiano o inglese) e rispondi nella stessa lingua. Sii conciso, pratico e utile.
"""
```

**For voice assistants** or **real-time chat**, reduce `num_ctx` to `512` for faster responses.

## 🛠️ Technical Details

- **Base Model**: [Google Gemma 3 1B IT](https://huggingface.co/google/gemma-3-1b-it)
- **Quantization**: Q4_0 and Q4_K_M (llama.cpp)
- **Context Length**: 1024 tokens (configurable down to 512)
- **Vocabulary Size**: 262,144 tokens
- **Architecture**: Gemma3ForCausalLM
- **Supported Platforms**: Raspberry Pi 4/5, Mac M1/M2, Linux ARM64, x86-64

## 🔒 Model Verification

Verify downloaded models using SHA256 checksums:

| File | SHA256 Checksum |
|------|----------------|
| `gemma3-1b-q4_0.gguf` | `d1d037446a2836db7666aa6ced3ce460b0f7f2ba61c816494a098bb816f2ad55` |
| `gemma3-1b-q4_k_m.gguf` | `c02d2e6f68fd34e9e66dff6a31d3f95fccb6db51f2be0b51f26136a85f7ec1f0` |

```bash
# Verify checksum (on Linux/Mac with Ollama)
# Models are stored in ~/.ollama/models/blobs/
sha256sum ~/.ollama/models/blobs/sha256-*
```

## 🔗 Links

- **Ollama**: https://ollama.com/antconsales/antonio-gemma3-smart-q4
- **HuggingFace**: https://huggingface.co/chill123/antonio-gemma3-smart-q4
- **GitHub** (demos, benchmarks, code): https://github.com/antconsales/gemma3-smart-q4

## 📜 License

This model is a **derivative work** of [Google's Gemma 3 1B](https://huggingface.co/google/gemma-3-1b-it).

**License**: Gemma License
Please review and comply with the [Gemma License Terms](https://ai.google.dev/gemma/terms) before using this model.

**Quantization, optimization, and bilingual configuration** by Antonio ([antconsales](https://github.com/antconsales)).

For licensing questions regarding the base model, refer to Google's official Gemma documentation.

---

## 📝 Version History

### v0.1.0 (2025-10-21)
- Initial release
- Two quantizations: Q4_0 (720 MB) and Q4_K_M (806 MB)
- Bilingual IT/EN support with automatic language detection
- Optimized for Raspberry Pi 4 (3.56-3.67 tokens/s)
- Tested on Raspberry Pi OS (Debian Bookworm) with Ollama

---

**Built with ❤️ for privacy and edge computing**
*Empowering offline AI, one Raspberry Pi at a time.* 🇮🇹
