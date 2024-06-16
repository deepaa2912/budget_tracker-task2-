#Description: Develop a console-based budget tracker that allows users to manage their expenses and income.
#Features:
#1. Expense and Income Entry: Allow users to input expenses and income with categories and amounts.
#2. Budget Calculation: Calculate the remaining budget after deducting expenses from income.
#3. Expense Analysis: Provide insights by categorizing expenses and displaying spending trends.
#4. Data Persistence: Store transactions in a file/database for tracking over time

import json
from datetime import datetime

DATA_FILE = "transactions.json"

def load_transactions():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_transactions(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)

def main():
    transactions = load_transactions()

    while True:
        print("\nBudget Tracker Application")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Calculate Budget")
        print("5. Expense Analysis")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_income(transactions)
        elif choice == "2":
            add_expense(transactions)
        elif choice == "3":
            view_transactions(transactions)
        elif choice == "4":
            calculate_budget(transactions)
        elif choice == "5":
            expense_analysis(transactions)
        elif choice == "6":
            save_transactions(transactions)
            break
        else:
            print("Invalid choice. Please try again.")

def add_income(transactions):
    amount = float(input("Enter income amount: "))
    category = input("Enter income category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    transaction = {
        "type": "income",
        "amount": amount,
        "category": category,
        "date": date
    }

    transactions.append(transaction)
    print("Income added successfully!")

def add_expense(transactions):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    transaction = {
        "type": "expense",
        "amount": amount,
        "category": category,
        "date": date
    }

    transactions.append(transaction)
    print("Expense added successfully!")

def view_transactions(transactions):
    print("\nTransactions:")
    for idx, transaction in enumerate(transactions):
        print(f"{idx + 1}. {transaction['date']} - {transaction['category']} - {'Income' if transaction['type'] == 'income' else 'Expense'}: ${transaction['amount']}")

def calculate_budget(transactions):
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    remaining_budget = total_income - total_expense

    print("\nBudget Calculation:")
    print(f"Total Income: ${total_income}")
    print(f"Total Expense: ${total_expense}")
    print(f"Remaining Budget: ${remaining_budget}")

def expense_analysis(transactions):
    categories = {}
    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            amount = transaction["amount"]
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\nExpense Analysis:")
    for category, amount in categories.items():
        print(f"Category: {category} - Total Spent: ${amount}")

if __name__ == "__main__":
    main()
