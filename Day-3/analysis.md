# Analysis: From Prompt to Action

## Scenario
I chose a simple scenario called "Student Fee Assistant". The system answers questions about course fees and basic calculations. Some questions require external data (fees), while others can be answered directly by the LLM.

---

## What is a Large Language Model?

A Large Language Model (LLM) is an AI system trained on large amounts of text data to understand and generate human-like responses.

In my scenario:
- The LLM can answer general questions like "What is Artificial Intelligence?"
- However, it cannot reliably give exact course fees because that data is not part of its training.
- It may guess or provide incorrect values.

---

## What is an Agent?

An agent is an LLM combined with tools and logic to perform actions beyond text generation.

In my scenario:
- The plain LLM simply answers based on its knowledge.
- The agent detects when a question requires external data and calls a tool to get accurate results.

---

## What is a Tool and Tool Call?

A tool is a function that performs a specific task (e.g., calculation or data lookup).

A tool call happens when:
1. The model identifies that it cannot answer directly.
2. It calls the tool.
3. The tool returns the result.
4. The model uses that result to generate the final answer.

In my scenario:
- `get_course_fee()` → returns fee
- `calculator()` → performs math

---

## Tool Call Flow (Step-by-Step)

Example: "What is the fee for CSE?"

1. User asks question
2. Agent detects keyword "fee"
3. Agent extracts "CSE"
4. Agent calls `get_course_fee("cse")`
5. Tool returns "100000"
6. Agent responds: "Fee for CSE is 100000"

---

## Why Tools Return Text

Tools return plain text instead of errors because:
- It prevents program crashes
- The agent can still respond gracefully
- It improves reliability

---

## Comparison Table

| Basis | Plain LLM | LLM with Tool |
|------|----------|--------------|
| Source of answer | Internal knowledge | External tool + LLM |
| Fetch external data | No | Yes |
| Reliability | Low for factual data | High |
| Transparency | Low | High |
| Speed | Fast | Slightly slower |

---

## Observation

### Question 1: What is the fee for CSE?
- Plain LLM: Incorrect / guessed answer
- Agent: Correct (100000)

### Question 2: What is 20000 + 5000?
- Plain LLM: Sometimes correct
- Agent: Always correct (25000)

### Question 3: What is Artificial Intelligence?
- Plain LLM: Correct
- Agent: Correct

---

## Suitability and Conclusion

The plain LLM is sufficient for general knowledge questions. However, when accurate data or calculations are required, tools are necessary.

In general:
- Use plain LLM → for explanations and general queries
- Use tools → for real-time, factual, or computational tasks

This shows that adding even one tool significantly improves correctness and reliability.