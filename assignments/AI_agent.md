# 🧠 Assignment: Build a Basic AI Agent with OpenAI Agents SDK

---

## 🎯 Objective

Develop a basic AI agent using the **OpenAI Agents SDK** that can perform a specific task within a chosen domain. This exercise will help you understand the foundational concepts of agent creation and interaction.

---

## 📌 Requirements

1. **Domain Selection**
    
    Choose a specific domain such as:
    
    - Education
    - Healthcare
    - Finance
    - Entertainment
    - Others
2. **Agent Development**
    - Define the agent's **purpose** and **capabilities** within the chosen domain.
    - Implement the agent using the **OpenAI Agents SDK**.
3. **Interaction**
    - Design sample **interactions or tasks** the agent can perform.
    - Ensure the agent provides **meaningful and accurate** responses.

---

## 📝 Example Agent: *MoodMate* — A Mental Health Check-In Assistant

> A simple and supportive AI agent that helps users express their feelings, reflect on their mental state, and receive gentle encouragement. MoodMate is not a medical advisor — it's a thoughtful friend.
> 

---

## 🛠️ Setup & Usage

### 1. **Create Project Using `uv`**

```bash
uv init --package moodmate
cd moodmate

```

> This will generate `pyproject.toml`, `.gitignore,` `README.md`, and set up a virtual environment.
> 

---

### 2. **Add Dependencies**

```bash
uv add openai-agents

```

---

### 3. **Set Your API Key in .env**

```bash
GEMINI_API_KEY=your-api-key

```

Replace `your-api-key` with your actual Gemini API key.

---

### 4. **Create the Agent Script**

Create a file named `moodmate.py` and add the following:

```python
from agents import Agent, Runner

moodmate = Agent(
    name="MoodMate",
    instructions="""
    You are MoodMate, a friendly and emotionally intelligent assistant.
    Your job is to help users reflect on their emotions and offer general tips for self-care.
    Be supportive, non-judgmental, and never offer medical advice.
    Use soft, comforting language and speak like a calm friend or life coach.
    Always end your response with a gentle question to encourage continued reflection.
    """
)

result = Runner.run_sync(moodmate, "I've been feeling anxious and low energy lately.")
print(result.final_output)

```

---

### 5. **Run the Agent**

```bash
uv run run_agent

```

---

## 💬 Example Interactions

### 🔹 Prompt:

**"I've been feeling really anxious and low energy lately."**

**🔸 Output:**

> I'm really sorry to hear that you're feeling this way. It's completely okay to feel anxious and drained — you're not alone. Sometimes our minds and bodies need a pause, and it's important to honor that.
> 
> 
> Have you had a chance to do something just for yourself lately, like a short walk, journaling, or deep breathing?
> 
> What’s one small thing you could do today that feels gentle and kind to yourself?
> 

---

### 🔹 Prompt:

**"I feel overwhelmed by tasks and responsibilities."**

**🔸 Output:**

> It sounds like you’re carrying a heavy load. That’s a lot for anyone. Remember, it's okay to take things one step at a time and prioritize self-care.
> 
> 
> Have you considered creating a to-do list to manage your tasks? Sometimes breaking things down can make them feel more manageable.
> 
> What’s one task you can focus on right now to ease your mind?
> 

---

## 📘 What You'll Learn

- How to define purpose-driven AI behavior
- How to work with the **OpenAI Agents SDK**
- How to structure prompts and reflect on outputs
- How to document your work like a real-world AI engineer

---

## 📦 Submission Instructions

1. Save the agent response in [`readme.md`](http://readme.md) file
2. **Push to GitHub**

```bash
git init
git add .
git commit -m "MoodMate AI agent"
git remote add origin https://github.com/your-username/moodmate.git
git branch -M main
git push -u origin main

```

> Replace your-username with your actual GitHub username.
> 

---

### 2. **Submit Your Link**

Submit your **GitHub repository link** in **Google Classroom** under this assignment.

---

> 💡 Tip: Build something empathetic. Good luck! 🌱
> 

---
