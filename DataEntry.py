
from datetime import datetime

# Date format used for parsing and displaying dates.
date_format = "%d-%m-%Y"
# Dictionary mapping input shorthand to full category names.
CATEGORIES = {"I": "Income", "E": "Expense"}

# Prompts the user to input a date. Optionally allows defaulting to today's date.
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%d-%m-%Y")
    try:
        valid_date = datetime.strptime(date_str, "%d-%m-%Y" )
        return valid_date.strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please enter a valid date in dd-mm-yyy format")
        return get_date(prompt, allow_default)

# Prompts the user to imput an amount and validates the input.
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-zero positive value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

# Prompts the user to input a category.
def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

def get_decription():
    return input("Enter a description (Optional): ")
