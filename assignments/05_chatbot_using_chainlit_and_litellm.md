# Assignment 05: Build a Chatbot Using Chainlit and LiteLLM

## 🎯 Objective

Create an intelligent chatbot using the **Chainlit** framework integrated with **LiteLLM**. The chatbot must support **streaming responses** and manage user conversations effectively. At the end of the session, the full chat history should be saved in a structured `chat_history.json` file. This assignment will help you understand conversational agents, response streaming, and persistence.

## 📌 Requirements

1. **Tech Stack**

   - Use **Chainlit** for the user interface
   - Use **LiteLLM** for handling LLM-based responses
   - **Do NOT use OpenAI Agent SDK**

2. **Functionality**

   - The chatbot should:

     - Accept user queries via a browser-based interface
     - Stream responses to users in real-time
     - Maintain and manage the **entire conversation history**
     - Automatically save the complete conversation in `chat_history.json` once the session ends

3. **Persistence**

   - The saved JSON file must include:

     - All user prompts
     - Corresponding bot responses (fully streamed)

   - Save this file automatically upon session completion

4. **Hints**

   - Study the **LiteLLM documentation**: [https://docs.litellm.ai/docs/](https://docs.litellm.ai/docs/)
   - Review the following GitHub repo for implementation help:
     [AI_201-Batch_67 Repo – Class 06](https://github.com/hassan-ak/AI_201-Batch_67-Q2-Certified_Agentic_Robotic_AI_Engineer/tree/main/class06-20250525)

## 📦 Submission Instructions

1. Include the following in your project repository:

   - Complete Python source code
   - The generated `chat_history.json` file
   - A `README.md` file that includes:

     - A **screenshot of the chatbot running in the browser**

2. Push to GitHub

3. Submit Your Link

   - Submit your **GitHub repository link** in **Google Classroom** under this assignment.

### 📝 Important Note

This assignment will be **marked during the next onsite session**. Make sure your implementation is complete and ready for demonstration.
