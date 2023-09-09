# Prompting the input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
oper = input("Enter the operation u wanna perform: \n ('/' for division, '+' for addition, '-' for subtration, \n 'x' for multilication): ")
if oper == '+':
    print(num1 + num2)
elif oper == '-':
    print(num1 - num2)
elif oper == 'x':
    print(num1 * num2)
elif oper == '/':
    print(num1 / num2)
else:
    print("Invalid symbol")