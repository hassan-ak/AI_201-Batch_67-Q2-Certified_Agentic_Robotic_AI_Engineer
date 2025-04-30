# Assignment 02: Create a "Hello World" Agent using OpenAI Agent SDK

## Objective

Build a simple "Hello World" agent using the OpenAI Agent SDK. This assignment is designed to introduce students to creating agents with proper package structure using the **UV package manager**, following best practices such as using `.env` files for secrets.

## Problem Statement

You are tasked with creating your first agent using the **OpenAI Agent SDK**. This agent will be a basic example to get you started with agent development. The agent should be structured within a UV-managed Python package named `hello-agent`, and demonstrate your ability to run it using a UV script.

## Why It's Exciting

- **Hands-on with OpenAI Agent SDK:** Start working with agents using a modern, production-ready framework.
- **Best Practices:** Learn proper Python packaging, use of environment variables, and clean script execution.
- **Real-World Skills:** Gain experience in setting up and organizing code for extensibility and reuse.

## Requirements

1. **Project Structure:**

   - Use the **UV package manager** to create a new package named `hello-agent`.
   - Inside your package, create a Python file named `agent_hello.py`.

2. **Function Definition:**

   - In `agent_hello.py`, define a function named `my_first_agent`.
   - Implement the agent logic inside this function using the **OpenAI Agent SDK**.
   - Ensure your function prints a basic “Hello, world!” response using the agent.

3. **Environment Configuration:**

   - Store any API keys or secrets in a `.env` file.
   - Load the environment variables securely in your code (e.g., using `python-dotenv`).

4. **Script Execution:**

   - Define a **UV script** in your `pyproject.toml` that allows you to run the agent using a command like:
     ```bash
     uv run <some-script>
     ```

5. **README and Documentation:**

   - Create a `README.md` file in the root of your project.
   - Include:
     - Step-by-step instructions to run your agent.
     - A **screenshot** of your terminal output after running the agent successfully.
   - Add comments in your Python code to explain what the agent is doing.

6. **Submission:**

   - Create a public **GitHub repository** for your project.
   - Push all your project files and commit history.
   - Submit the link to your GitHub repository as your assignment submission.

## Note

- The assignment submission **deadline** is **2025-05-03** at **11:59 PM**.
- **This assignment is compulsory** and must be completed **before attending the next onsite class**.
- Late submissions will **not be accepted** under any circumstances.