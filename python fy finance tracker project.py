from datetime import datetime

income = 0.0
budget_limit = 0.0
budgets = {}  # category: amount
expenses = {}  # category: list of (date, amount)

# Set income and budget limit
def set_income():
    global income, budget_limit
    income = float(input("Enter your monthly income: "))
    budget_limit = float(input("Set your total budget limit: "))
    print(f"Income: ${income:.2f}, Budget Limit: ${budget_limit:.2f}\n")

# Add budget categories
def add_budget():
    while True:
        category = input("Enter budget category: ").strip().title()
        amount = float(input("Enter budget amount: "))
        budgets[category] = amount
        expenses[category] = []  # Initialize expense list for this category
        print(f"Added budget: [{category}] - ${amount:.2f}\n")
        another = input("Do you want to add another budget? (yes/no): ").strip().lower()
        if another != 'yes':
            break

# Add expense for existing budget categories
def add_expense():
    if not budgets:
        print("No budget categories available. Please add a budget first.")
        return

    print("\nAvailable categories:")
    for i, cat in enumerate(budgets.keys(), 1):
        print(f"{i}. {cat}")
    try:
        choice = int(input("Select a category number to add expense to: "))
        category = list(budgets.keys())[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    amount = float(input("Enter expense amount: "))
    date = datetime.now().strftime("%Y-%m-%d")
    expenses[category].append((date, amount))
    print(f"Added expense: [{date}] [{category}] - ${amount:.2f}\n")

# Show budgets
def show_budgets():
    if not budgets:
        print("No budgets recorded yet.")
    else:
        print("\n--- Budgets ---")
        for i, (cat, amt) in enumerate(budgets.items(), 1):
            print(f"{i}. [{cat}]: ${amt:.2f}")

# Show expenses
def show_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\n--- Expenses ---")
        for cat, entries in expenses.items():
            for date, amt in entries:
                print(f"[{date}] [{cat}]: ${amt:.2f}")

# Total spent
def total_spent_all():
    return sum(amt for cat in expenses.values() for (_, amt) in cat)

# Summary
def display_summary():
    total_budgeted = sum(budgets.values())
    total_spent = total_spent_all()
    remaining_budget = total_budgeted - total_spent
    remaining_limit = budget_limit - total_spent

    print("\n--- Summary ---")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Budgeted: ${total_budgeted:.2f}")
    print(f"Total Expenses: ${total_spent:.2f}")
    print(f"Remaining Budget (Budgeted - Expenses): ${remaining_budget:.2f}")
    print(f"Remaining Budget Limit (Limit - Expenses): ${remaining_limit:.2f}")

    if total_spent > budget_limit:
        print("Warning: You exceeded your budget limit!")
    elif total_spent > budget_limit * 0.9:
        print("Caution: You're nearing your budget limit.")
    else:
        print("You're managing your budget well!")

    print("\n--- Category-wise Spending ---")
    for cat in budgets:
        spent = sum(amt for (_, amt) in expenses[cat])
        print(f"{cat}: Spent ${spent:.2f} / Budget ${budgets[cat]:.2f}")
        if spent > budgets[cat]:
            print(f"  -> Exceeded budget in category '{cat}'!")

# Menu
def main():
    set_income()
    while True:
        print("\nOptions:")
        print("1. Add Budget")
        print("2. Add Expense")
        print("3. View Budgets")
        print("4. View Expenses")
        print("5. View Summary")
        print("6. Exit")
        choice = input("Choose an option:\n ")

        if choice == "1":
            add_budget()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_budgets()
        elif choice == "4":
            show_expenses()
        elif choice == "5":
            display_summary()
        elif choice == "6":
            print("Goodbye! Stay on budget.")
            break
        else:
            print("Invalid choice. Please try again.")

main()