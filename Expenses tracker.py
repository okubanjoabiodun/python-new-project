expenses = []

while True:
    print("\n ------EXPENSES TRACKER------")
    print("1. Add expenses")
    print("2. Edit expenses")
    print("3. View expenses")
    print("4. Delete expenses")
    print("5. Exit")

    choice = input("Enter option: ")

    # Add expense
    if choice == "1":
        title = input("Add expense title: ")
        expense = {
            "title": title,
            "completed": False
        }
        expenses.append(expense)
        print("Expense created successfully.")

    # Edit expense
    elif choice == "2":
        if not expenses:
            print("No expenses recorded")
            continue

        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['title']}")

        number = int(input("Enter expense number to edit: "))

        if 1 <= number <= len(expenses):
            new_title = input("Enter new expense name: ")
            expenses[number - 1]["title"] = new_title
            print("Expense updated successfully!")
        else:
            print("Invalid expense number.")

    # View expenses
    elif choice == "3":
        if not expenses:
            print("No expenses recorded.")
        else:
            for i, expense in enumerate(expenses, 1):
                status = "Completed" if expense["completed"] else "Not completed"
                print(f"{i}. {expense['title']} - {status}")

    # Delete expense
    elif choice == "4":
        if not expenses:
            print("No expenses recorded.")
            continue

        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['title']}")

        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            print(f"Expense '{deleted['title']}' deleted successfully.")
        else:
            print("Invalid expense number.")

    # Exit
    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid option. Please try again.")
             
             
             
    