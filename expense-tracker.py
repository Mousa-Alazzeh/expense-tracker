import json

expenses_list = []


# Step 1: Add Expenses
def add_expense(amount, category):
    expense = {"amount": amount, "category": category}
    expenses_list.append(expense)
    write_expenses_to_file()


# Step 2: Write Expenses to File
def write_expenses_to_file():
    with open("expenses.txt", "w") as file:
        json.dump(expenses_list, file)


# Step 3: Load Expenses from File
def load_expenses_from_file():
    global expenses_list
    try:
        with open("expenses.txt", "r") as file:
            expenses_list = json.load(file)
    except FileNotFoundError:
        expenses_list = []
    return expenses_list


# Step 4: Update Expenses
def update_expense(old_expense, new_expense):
    if old_expense in expenses_list:
        index = expenses_list.index(old_expense)
        expenses_list[index] = new_expense
        write_expenses_to_file()


# Step 5: Calculate Total Expenses
def calculate_total_expenses():
    total = 0
    for expense in expenses_list:
        total += expense["amount"]
    return total


# Step 6: Calculate Total Expenses by Category
def calculate_expenses_by_category(category):
    category_total = 0
    for expense in expenses_list:
        if expense["category"] == category:
            category_total += expense["amount"]
    return category_total
