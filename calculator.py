#create a simple calculator program for two unknown numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":   
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print("The result is:", result)