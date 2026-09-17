print("Welcome to expense calculator")
expenses = {}

while True:
    expense_name = input("Enter expense name (or done): ")
    if expense_name.lower() == "done":
        break
    price = float(input("Enter price: "))
    expenses[expense_name.upper()] = price

print("\nYOUR EXPENSES:")
for name, price in expenses.items():
    print(f"{name}: {price}")
print(f"TOTAL: {sum(expenses.values())}")