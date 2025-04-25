## OpenRouter: A Unified Interface for 50+ Free LLMs

**Table of Content**
- [OpenRouter: A Unified Interface for 50+ Free LLMs](#openrouter-a-unified-interface-for-50-free-llms)
- [1. Quickstart](#1-quickstart)
- [2. Features](#2-features)
- [3. Rate Limits \& Free Models](#3-rate-limits--free-models)
  - [3.1 Free Models Rate Limits](#31-free-models-rate-limits)
  - [3.2 Google Gemini (Free Tier)](#32-google-gemini-free-tier)
- [4. Architecture \& Hosting](#4-architecture--hosting)
- [5. Model Catalog](#5-model-catalog)
- [6. References](#6-references)


**Code Example:** [Basic and OpenAI Agents SDK with OpenRouter](https://colab.research.google.com/drive/1LOEOBP52WJpmMWsOS7-SUDQBLtmXZ_1d?usp=sharing)

OpenRouter provides a single, consistent API for accessing over 200 large language models (LLMs), including 50+ free variants that support the de facto OpenAI Chat Completion API. Whether you're integrating open-source models like Mistral or LLaMA or commercial offerings from OpenAI and Anthropic, OpenRouter handles routing, translation, and authentication to optimize cost, latency, and uptime.

## 1. Quickstart

1. **Get an API Key**  
   Sign up at [openrouter.ai](https://openrouter.ai/) and copy your API key.

2. **Choose a Model**  
   Models ending with `:free` are free-tier and subject to rate limits (see §3).  
   Example: `deepseek-chat-v3-0324:free`

3. **Install the SDK**

   ```bash
   pip install openrouter
   ```

4. **Python Example**

   ```python
   import openrouter

   client = openrouter.OpenRouter(api_key="YOUR_API_KEY")
   response = client.chat.completions.create(
       model="deepseek-chat-v3-0324:free",
       messages=[
           {"role": "user", "content": "Hello, world!"}
       ]
   )
   print(response.choices[0].message.content)
   ```

5. **OpenAI Agents SDK**  
   Simply update the environment variables:
   ```bash
   export OPENAI_API_KEY="YOUR_API_KEY"
   export OPENAI_API_BASE="https://openrouter.ai/api/v1"
   ```

## 2. Features

- **Multi-Provider Routing**  
  Routes requests to the best provider based on price, latency, and availability.

- **OpenAI API Compatibility**  
  Mirrors OpenAI endpoints (`/v1/chat/completions`), parameters, and SDK support.

- **Function (Tool) Calling**  
  Supports OpenAI-style `functions` parameter for invoking external tools.  
  See [Tool & Function Calling](https://openrouter.ai/docs/features/tool-calling).

- **Streaming & Logging**  
  Optional streaming responses and prompt logging (opt-in).

- **Playground & UI**  
  An interactive chatroom at [openrouter.ai/chat](https://openrouter.ai/chat) for testing multiple LLMs side-by-side.

## 3. Rate Limits & Free Models

### 3.1 Free Models Rate Limits

All free-tier models (`:free`) share a **200 requests/day** (RPD) quota. Most also impose a **20 requests/minute** (RPM) cap.

> **Note:** Limits may vary by provider. Always refer to the [API Rate Limits Reference](https://openrouter.ai/docs/api-reference/limits) for details.

### 3.2 Google Gemini (Free Tier)

For development and testing, Google Gemini Flash models offer higher quotas:

- **Gemini 2.0 Flash & Flash-Lite**
  - 1,500 RPD
  - 15 RPM (Flash), 30 RPM (Flash-Lite)
  - 1,000,000 TPM

**Recommendation:** Use Gemini Flash models for non-production testing, since OpenRouter’s free-tier RPD (200) may be restrictive.

Gemini supports the OpenAI Chat Completion API:  
https://ai.google.dev/gemini-api/docs/openai

## 4. Architecture & Hosting

- **Proxy Model:**  
  OpenRouter proxies requests to third-party providers (e.g., TogetherAI, AWS, Anthropic), without hosting the models itself.

- **Provider Routing:**  
  Intelligent routing for cost/performance, with failover and load balancing.  
  See [Provider Routing](https://openrouter.ai/docs/features/provider-routing).

## 5. Model Catalog

Browse all available models (free and paid):  
https://openrouter.ai/models

> **Free Models:** 50+ models with zero cost per token, including 6 with 1M+ context windows.

## 6. References

- [OpenRouter Quickstart Guide](https://openrouter.ai/docs/quickstart)
- [Connecting to OpenRouter from Python](https://medium.com/@tedisaacs/from-openai-to-opensource-in-2-lines-of-code-b4b8d2cf2541)
- [Tool & Function Calling](https://openrouter.ai/docs/features/tool-calling)
- [API Rate Limits](https://openrouter.ai/docs/api-reference/limits)
- [Provider Routing](https://openrouter.ai/docs/features/provider-routing)
- [OpenRouter Chat Playground](https://openrouter.ai/chat)

---