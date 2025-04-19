# Class 02 - 2024/04/20 - Batch 67 - Q2 (Certified Agentic Robotic AI Engineer)

## Programming Language, Library, Framework and SDK

| Term                               | Simple Definition                                                                 | Real-Life Analogy                                                                | How You Use It                                                           | Examples                            |
| ---------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------- |
| **Programming Language**           | The language you use to write instructions for the computer.                      | Like English or Urdu – a way to **communicate**.                                 | You use it to write all your code.                                       | Python, JavaScript, Java, C++       |
| **Library**                        | A set of pre-made tools or code that helps you do common tasks more easily.       | Like a **calculator** – you use it to save time doing math.                      | You **import** it and use its functions in your code when you need them. | NumPy (Python), jQuery (JavaScript) |
| **Framework**                      | A bigger structure or system that helps you build apps faster and more organized. | Like a **house blueprint** – you build your home inside a ready-made structure.  | You **follow its rules**, add your code inside it, and it runs the app.  | Django (Python), React, Laravel     |
| **SDK (Software Development Kit)** | A full package of tools to help you build apps for a specific platform.           | Like a **DIY furniture kit** – it gives you everything to build a specific item. | It comes with libraries, tools, and guides to help you build apps.       | Android SDK, iOS SDK, .NET SDK      |

### Building a Weather App

| Part                   | What It Did                                |
| ---------------------- | ------------------------------------------ |
| **Python (Language)**  | Wrote the logic, connected everything.     |
| **Requests (Library)** | Helped you talk to websites easily.        |
| **Flask (Framework)**  | Turned your app into a web app.            |
| **Weather API SDK**    | Gave a shortcut to use their weather data. |

---

## AI, GenAI and AI Agents

| **Concept**                      | **Description**                                                                                                            | **Example**                                                                       |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **AI (Artificial Intelligence)** | AI is when computers or machines are made to think and make decisions like humans.                                         | Your phone suggesting words while typing.                                         |
| **GenAI (Generative AI)**        | GenAI is a special type of AI that can _create_ new things like text, images, music, or code.                              | ChatGPT writing essays, stories, or answering questions.                          |
| **AI Agents**                    | AI agents are smart programs that can _act_ on their own to do tasks. They use AI to make decisions and work step-by-step. | A helper robot that plans, searches the web, and provides summaries autonomously. |

---

## Simple Software, AI Model and LLM

| Feature                  | Simple Software                         | AI Model                              | LLM (Large Language Model)                  |
| ------------------------ | --------------------------------------- | ------------------------------------- | ------------------------------------------- |
| **Definition**           | Follows fixed instructions              | Learns patterns from data             | AI model focused on human language tasks    |
| **Created by**           | Fully coded by humans                   | Trained using data                    | Trained on massive text data                |
| **Learning Ability**     | ❌ No learning                          | ✅ Learns from training data          | ✅ Learns language, grammar, logic, context |
| **Example Task**         | Calculator, weather app, booking system | Face recognition, product suggestions | Chatbot, essay writer, translator           |
| **Output Type**          | Fixed and predictable                   | Predictive or dynamic                 | Text (answers, code, summaries, stories)    |
| **Can Handle Language?** | Very limited                            | Somewhat, with effort                 | ✅ Expert in language                       |
| **Changes Over Time?**   | Only if updated manually                | Yes — retrains and improves           | Yes — gets better with new training         |

### 🧠 Real-Life Analogy

| Thing           | Analogy                                                                              |
| --------------- | ------------------------------------------------------------------------------------ |
| Simple Software | A **vending machine** – you press buttons, it gives the same thing every time.       |
| AI Model        | A **student** – you show examples, and they learn to make their own decisions.       |
| LLM             | A **language expert student** – trained by reading everything, can write/talk/think. |

---

## What is an API?

**API** stands for **Application Programming Interface**.

Think of it as a **waiter** in a restaurant.

- You (the user) sit at a table and look at the **menu**.
- You don’t go into the kitchen and make your own food.
- Instead, the **waiter** takes your order to the kitchen and brings your food back to you.

➡️ In the same way, an **API** is a messenger that lets different software programs talk to each other.

### Real Life example of API

Imagine you’re using a **weather app** on your phone.

- That app doesn’t have all the weather data inside it.
- It sends a **request** to a weather service **API** (like asking the kitchen for food).
- The weather service sends back the **data** (the food).
- The app then shows you today’s temperature.

### 🧠 In Simple Words:

An **API** lets one app or website **ask** another app or website for **information** or **services**.

- It’s like a **bridge** between two programs.
- You don’t need to know how the other program works, you just use the API.

---

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