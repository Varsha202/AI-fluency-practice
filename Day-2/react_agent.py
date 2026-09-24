from tools.expense_tool import get_total_by_category, get_highest_category

def react_agent(question):
    print("Question:", question)

    if "food" in question.lower():
        print("Thought: Need to check food expenses")
        print("Action: get_total_by_category('Food')")
        result = get_total_by_category("Food")
        print("Observation:", result)
        print("Final Answer:", result)

    elif "highest" in question.lower():
        print("Thought: Find highest category")
        print("Action: get_highest_category()")
        result = get_highest_category()
        print("Observation:", result)
        print("Final Answer:", result)

react_agent("Which category has highest spending?")