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