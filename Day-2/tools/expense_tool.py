import pandas as pd

def get_total_by_category(category):
    df = pd.read_csv("data/expenses.csv")
    return df[df["category"] == category]["amount"].sum()

def get_total_spend():
    df = pd.read_csv("data/expenses.csv")
    return df["amount"].sum()

def get_highest_category():
    df = pd.read_csv("data/expenses.csv")
    return df.groupby("category")["amount"].sum().idxmax()