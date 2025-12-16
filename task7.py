num1 = float(input("First number: "))
operation = input("Operation (+, -, *, /): ")
num2 = float(input("Second number: "))

if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "/":
    # Сокращенная форма условия прямо в print
    print(f"{num1} / {num2} = {num1 / num2 if num2 != 0 else 'Error! Division by zero'}")
else:
    print("Error! Unknown operation")