# Assignment 06: Build an OpenAI Agent SDK-Based Chatbot with Chainlit

## 🎯 Objective

Develop a **smart, multi-tool chatbot** using the **OpenAI Agent SDK** integrated with **Chainlit**. The chatbot should support **streaming responses**, manage **complete chat history**, and integrate **two or more tools**—one of which must invoke an **external API**, and another must be an **agent tool**. You will also use **Chainlit chat profiles** to provide users with customization options, such as model selection or other functionality.

## 📌 Requirements

1. **Tech Stack**

   * **Chainlit** for the user interface
   * **OpenAI Agent SDK** to manage the agent
   * At least **two tools**:

     * One that connects to an **external API**
     * One custom agent-based
   * Use **Chainlit Starter Prompts** for better user experience
   * Use **Chainlit Chat Profiles** for customization

2. **Functionality**

   The chatbot must:

   * Accept user input from a browser-based interface
   * **Stream responses in real time** (i.e., character-by-character generation)
   * Use at least **two tools**:

     * One tool calling an **external API**
     * One **custom agent-based or internal tool**
   * Maintain the **entire chat history**
   * Automatically save the chat into a `chat_history.json` file at the end of the session
   * Display the following in the Chainlit UI:

     * A **placeholder message** such as “Thinking...” while generating a response
     * Any **tool invocation** should be visible in the chat interface
     * Some **starter messages** at the beginning of each chat session
   * Use **Chainlit chat profiles** to allow users to **customize their experience**, such as:

     * Selecting different LLM **models**
     * Choosing a chatbot **mode** (e.g., casual vs. technical)
     * Enabling/disabling specific **tools**

3. **Persistence**

   * The `chat_history.json` file must include:

     * All user messages
     * All bot responses

4. **Hints**

   * OpenAI Agent SDK Documentation:
     [https://openai.github.io/openai-agents-python/](https://openai.github.io/openai-agents-python/)
   * Chainlit Chat Profiles Documentation:
     [https://docs.chainlit.io](https://docs.chainlit.io)
   * Recommended file structure:

## 📦 Submission Instructions

1. Include the following in your project repository:

   * All source code files
   * `chat_history.json` file (generated after a chat session)
   * `README.md` with:

     * A brief explanation **in your own words** of what your chatbot does
     * A **screenshot** of the chatbot running in the browser

2. Push your project to GitHub.

3. Submit Your Link

   * Submit your **GitHub repository link** in **Google Classroom** under this assignment.

---

### 📝 Important Note

This assignment will be **marked during the next onsite session**. Ensure your chatbot, tool integrations, profiles, and interface features are functional and demonstrable.
