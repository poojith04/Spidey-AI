# 🕷️ Spidey AI - Architecture

## Overview

Spidey is a modular personal AI assistant designed to grow from a simple chatbot into a full AI operating system.

---

## Current Architecture (v0.3)

```
User
  │
  ▼
main.py
  │
  ▼
Assistant
  ├── Brain
  ├── Memory (Conversation)
  ├── Personality
  └── Response Formatter
```

---

## Components

### Brain
- Connects to Gemini
- Sends prompts
- Receives AI responses

### Memory
- Stores conversation history during the current session

### Personality
- Defines Spidey's identity, greetings, and behavior

### Response Formatter
- Formats AI responses to match Spidey's speaking style

---

## Upcoming Components

- SQLite Memory (Persistent Memory)
- Knowledge Memory (RAG)
- Tool Manager
- Voice Engine
- Vision Engine
- Planner
- Plugin System

---

## Project Goal

Create a personal AI assistant that can:

- Remember the user
- Search personal knowledge
- Control the computer
- Understand voice and images
- Execute tasks
- Grow through plugins