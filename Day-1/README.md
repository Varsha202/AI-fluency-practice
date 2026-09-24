# Agentic AI – Day 1 Practice Task

## Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

This project is part of the Day 1 practice task for Agentic AI.

The objective is to compare three approaches for solving the same college event registration scenario:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

The comparison focuses on flexibility, decision-making, tool usage, private-data access, multi-step task handling, automation, and reliability.

---

## Scenario

The chosen scenario is **College Event Registration**.

The application contains private event information:

| Event | Registration Fee | Capacity |
|---|---:|---:|
| TECHFEST2026 | ₹500 | 100 |
| HACKATHON2026 | ₹300 | 50 |
| AIWORKSHOP2026 | ₹200 | 30 |

---

## Questions Tested

The three systems were tested using the same set of questions:

1. What is the registration fee for TECHFEST2026?
2. What is the total cost of TECHFEST2026 and AIWORKSHOP2026 after a 10% discount?
3. Is TECHFEST2026 more expensive than AIWORKSHOP2026? If yes, by how much?
4. Give me a two-line welcome message for the college events.

---

## Approaches Implemented

### 1. Plain Chatbot

The plain chatbot uses a Groq-hosted LLM to generate responses.

It does not directly access the private event data stored in the application.

File:

```text
chatbot.py
