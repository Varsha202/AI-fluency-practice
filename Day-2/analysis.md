# Reasoning and Acting: Direct Prompting vs Chain-of-Thought vs ReAct

## Scenario
The chosen scenario is a Personal Expense Assistant. It answers questions related to expenses such as total spending, highest category, and budget analysis. Some questions require external data (CSV file), while others require reasoning.

---

## 1. Explanation of Each Approach

### Direct Prompting
Direct prompting provides an answer immediately based on the model’s internal knowledge. It does not show reasoning steps and does not use any external tools. In this scenario, it fails to accurately answer questions that require real data, such as total food spending, because it cannot access the CSV file.

---

### Chain-of-Thought Prompting
Chain-of-Thought prompting makes the model think step by step before answering. This improves reasoning ability for multi-step problems. However, it still cannot access external data. In this scenario, it correctly solves arithmetic questions but fails when actual expense data is required.

---

### ReAct Agent
ReAct combines reasoning and acting. The agent first thinks about what is needed, then performs an action (tool call), observes the result, and continues reasoning. In this scenario, it successfully uses the expense tool to fetch real data and produce accurate answers.

---

## 2. Comparison Table

| Basis | Direct Prompting | Chain-of-Thought | ReAct Agent |
|------|----------------|------------------|------------|
| Reasoning depth | Low | High | High |
| Tool usage | No | No | Yes |
| Reliability | Low | Medium | High |
| Transparency | Low | High | High |
| Speed | Fast | Medium | Slower |
| Consistency | High | Medium | Medium |

---

## 3. Self-Consistency Observation

The Chain-of-Thought approach was run multiple times with temperature 0.7. The answers varied slightly in reasoning but the final answer was mostly the same. The majority answer was correct. When temperature was set to 0, the output became consistent and identical across runs.

---

## 4. Suitability Analysis

For this scenario, the ReAct agent is the most suitable approach. This is because the problem requires both reasoning and access to external data. Direct prompting fails due to lack of data access, and Chain-of-Thought improves reasoning but still cannot fetch real data. ReAct successfully integrates both reasoning and tool usage.

---

## 5. Conclusion

Direct prompting is best for simple questions that do not require reasoning or external data. Chain-of-Thought is useful for problems that require logical reasoning and step-by-step thinking. ReAct is the most powerful approach for real-world applications where both reasoning and external tool usage are required.