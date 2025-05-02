# Class 03 - 2024/04/27 - Batch 67 - Q2 (Certified Agentic Robotic AI Engineer)

**Table of Content**
- [Class 03 - 2024/04/27 - Batch 67 - Q2 (Certified Agentic Robotic AI Engineer)](#class-03---20240427---batch-67---q2-certified-agentic-robotic-ai-engineer)
  - [Chat Completions API vs Responses API](#chat-completions-api-vs-responses-api)
    - [Chat Completions API](#chat-completions-api)
    - [Responses API](#responses-api)
  - [Design patterns](#design-patterns)


## Chat Completions API vs Responses API

### Chat Completions API
The Chat Completions API enables developers to generate AI-driven conversational responses based on a sequence of input messages. This API operates on a stateless model, meaning each request requires the full conversation history to provide context. Developers structure inputs as a list of messages, and the model generates a corresponding reply. This approach is particularly useful for applications requiring straightforward conversational AI without the need for complex state management.

### Responses API
Introduced as an evolution of OpenAI’s API offerings, the Responses API combines the simplicity of the Chat Completions API with advanced functionalities to support more dynamic and interactive AI applications. 

Key features include:
- Stateful Interactions: Unlike the stateless Chat Completions API, the Responses API maintains state across interactions, allowing for seamless continuation of conversations without resending the entire history.
- Built-in Tools: The API integrates tools such as web search, file search, and computer use, enabling AI agents to perform tasks like retrieving real-time information, accessing documents, and executing operations on a user’s behalf.
- Enhanced Flexibility: With a more flexible structure, the Responses API supports complex workflows and agentic behaviors, making it suitable for developing sophisticated AI agents capable of handling a variety of tasks.

---

## Design patterns

Design patterns are proven, reusable solutions to common problems in software design. They act like templates or best practices that help developers write cleaner, more efficient, and maintainable code. Instead of reinventing the wheel, developers use these patterns to solve problems in a standardized way, making code easier to understand and collaborate on.