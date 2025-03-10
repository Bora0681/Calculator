def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

while True:
    operation = input("Enter operation (+, -, *, /) or type 'exit': ").lower()
    if operation == 'exit':
        break
    num1 = float(input('Please, enter the first number: '))
    num2 = float(input('Please, enter the second number'))
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = substract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    elif operation =='exit':
        break
    else:
        result = "Invalid operation!"
    print("Result:", result)
    print("sa")


