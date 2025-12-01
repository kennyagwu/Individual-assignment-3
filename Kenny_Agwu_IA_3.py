# Problem 1: Simple Calculator
# This program performs addition, subtraction, multiplication, or division
# using two numbers entered by the user.

# Ask user to enter first number
num1 = float(input("Enter the first number: "))

# Ask user to enter an operator
operator = input("Enter an operator (+, -, *, /): ")

# Ask user to enter second number
num2 = float(input("Enter the second number: "))

# Perform operation using if/elif/else
if operator == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} = {result:.2f}")
elif operator == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} = {result:.2f}")
elif operator == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} = {result:.2f}")
elif operator == '/':
    # Check if the second number is zero before dividing
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} = {result:.2f}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please enter +, -, * or /.")

# Problem 2: Sales Target Tracker
# This program tracks cumulative sales for a 5-day week
# and shows progress toward a target entered by the user.

# Ask user for total sales target
target = float(input("Enter total sales target: "))

# Initialize total sales to 0
totalSales = 0

# Use a for loop to track sales for 5 days
for day in range(1, 6):
    sales = float(input(f"Enter day {day} sales: "))
    totalSales += sales  # add current day's sales to total

    # Calculate cumulative percentage
    percent = (totalSales / target) * 100

    # Display cumulative progress
    print(f"Cumulative sales: {totalSales:.1f} ({percent:.1f} %)")
