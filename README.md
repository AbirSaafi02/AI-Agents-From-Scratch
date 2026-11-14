# TinyAgent 🤖

A minimal, modular, and educational AI agent framework built entirely from scratch, inspired by [*An Illustrated Guide to AI Agents*](https://github.com/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents). 

## Overview & Concept
The goal of this project is to build an AI Agent step-by-step to truly understand what happens "under the hood" (how LLMs reason, handle memory, call tools, and plan actions), rather than treating them as a black box. 

I found this approach super easy and insightful to grasp the core architecture of modern AI agents!

---

## Chapter 1: The Skeleton Architecture (`agent.py`)

In this first chapter, we set up the foundational skeleton of our `TinyAgent`. It doesn't have a "brain" (LLM) yet, but it defines the modular structure we will expand in upcoming chapters:

* **`__init__`**: Placeholders for future modules (LLM, Memory, Tools, Planner).
* **`run()`**: Executes the agent on a given task.
* **`_step()`**: Handles a single step of processing.
* **`_execute_action()`**: Placeholder for executing tool actions (APIs, calculations).

### Code Implemented in src/agent.py

## Chapter 2 — Adding the "Brain" & The LLM Wrapper

In this chapter, we transition our TinyAgent from a simple structural skeleton into an autonomous agent by plugging in its Brain (the Large Language Model).

What makes this approach particularly powerful and flexible is how the authors designed the architecture around two core concepts:

1. The Power of the OpenAI-Compatible Standard
Instead of forcing a single LLM provider or locking us into a complex ecosystem, the project leverages the OpenAI API standard format (/v1/chat/completions).

Why it matters: Almost all modern inference engines (whether running locally via Ollama or LM Studio, or in the cloud via OpenRouter or Google) expose this exact same endpoint format.

The Developer Benefit: You can switch from a free local model (like Gemma 4) to a cloud model simply by changing three configuration variables (base_url, model, and api_key) without changing a single line of your core agent logic.

2. The LLM Wrapper (class LLM dans llm.py)
To abstract away all the repetitive HTTP plumbing (building JSON payloads, handling POST requests, parsing raw responses), we introduce a lightweight LLM Wrapper.

What it does: It acts as a universal adapter. It takes the agent's messages, formats them into the standard JSON request, sends it to whichever server you choose, and normalizes the incoming response into a clean Python dataclass (Response).

Why we use it: It keeps the TinyAgent code clean, readable, and decoupled from any specific API provider's quirks.

3. Execution Tracking: The Trajectory (`Step` & `Trajectory` in `trajectory.py`)
As agents evolve to handle multi-step reasoning and tool calls, debugging becomes a major challenge. To make the agent's internal decision-making transparent, we introduce execution tracking.

* **What it does:** Every run starts with a user `query` and records a sequence of `Step` objects. Each step captures the agent's internal `thought`, the `action` (tool call) it took, the `observation` (output returned by the tool), the final `answer`, and token `metadata`.

* **Why it matters:** Without a trajectory, an agent is a black box. Tracking each step gives us full visibility into the agent's execution flow and lays the foundation for the **THOUGHT → ACTION → OBSERVATION** loop we will implement in later chapters.

* my choice : Ollama + Qwen
I'm running everything locally using **Ollama** with **Qwen**. With limited PC resources and zero budget for paid API keys, this combo is the sweet spot—it's lightweight, fast enough for local testing, and completely free.