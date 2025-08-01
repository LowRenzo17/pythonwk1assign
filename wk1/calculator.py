# Get user input for numbers and operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
        exit()
    result = num1 / num2
else:
    print("Error: Invalid operation! Please use +, -, *, or /.")
    exit()

# Display the equation and result
print(f"{num1} {operation} {num2} = {result}")