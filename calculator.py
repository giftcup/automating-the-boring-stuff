num1 = int(input("First number: "))
num2 = int(input("Second number: "))

operation = input("Select an operation from *, /, +, -: ")

if operation == '*':
    result = num1 * num2
elif operation == '/' and num2 != 0:
    result = num1 / num2
elif operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
else:
    print("Operation is invalid")
    exit()
print(f"{num1} {operation} {num2} = {result}")
