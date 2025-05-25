# Use OpenRouter With OpenAI Agents SDK

**Table of Content**

- [Use OpenRouter With OpenAI Agents SDK](#use-openrouter-with-openai-agents-sdk)
  - [Setup Prerequisite:](#setup-prerequisite)
  - [Free and Paid Models](#free-and-paid-models)
  - [Rate Limiting and Crediting](#rate-limiting-and-crediting)
  - [OpenRouter 404 Error Solution](#openrouter-404-error-solution)

## Setup Prerequisite:

1. [Signup at OpenRouter](https://openrouter.ai/)
2. [Create an API Key](https://openrouter.ai/settings/keys)
3. Select a Free Model (you can continue as we are using a free model here)

## Free and Paid Models

The OpenRouter supports the latest DeepSeek V3 0324 and 50+ other models for free. Most of them support the defacto standard: OpenAI Chat Completion API.

If you are using a free model variant (with an ID ending in :free), then you will be limited to 20 requests per minute and 200 requests per day.

**See all Models List: https://openrouter.ai/models**

**Note:** OpenRouter do not charge anything extra at inference time.

## Rate Limiting and Crediting

There are a few rate limits that apply to certain types of requests, regardless of account status:

- Free limit: If you are using a free model variant (with an ID ending in :free), then you will be limited to 20 requests per minute and 200 requests per day.

If your account has a negative credit balance, you may see 402 errors, including for free models. Adding credits to put your balance above zero allows you to use those models again.

[Reference](https://openrouter.ai/docs/api-reference/limits)

## OpenRouter 404 Error Solution

**NotFoundError: Error code: 404**

```python
{
    'error': {
        'message': 'No endpoints found matching your data policy. Enable prompt training here: https://openrouter.ai/settings/privacy',
        'code': 404
    }
}
```

**Cause**

- This error occurs when OpenRouter API can't find endpoints matching your data policy, typically because prompt training is disabled.

**Solution**

- Enable Prompt Training:
  - Visit OpenRouter Privacy Settings
  - Toggle ON "Prompt Training" option
  - Re-run your code after enabling
- Re-run your code after enabling

**Prevention**

- Keep prompt training enabled for uninterrupted API access.
