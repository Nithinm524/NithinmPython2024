# -*- coding: utf-8 -*-
"""Personal Expense Tracker.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VXJexpWSfjnL8fGQkl82Pp-oCj-rR2KF
"""

def add_expense(expenses):
    category = input("Enter the category (e.g., Food, Rent): ")
    amount = float(input("Enter the amount: "))
    expenses.append({"category": category, "amount": amount})
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']}: ${expense['amount']:.2f}")
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    expenses = []
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")