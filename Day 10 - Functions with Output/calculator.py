from art import logo
print(logo)
"""
def add(n1, n2):
    takes n1 and n2 and add it together
    return n1 + n2

def sub(n1, n2):
    finds the difference between n1 from n2
    return n1 - n2

def multiply(n1, n2):
    multiply n1 by n2
    return n1 * n2

def divide(n1, n2):
    find the division from n1 and n2
    return n1 / n2

operations = {
    "+": "add",
    "-": "sub",
    "*": "multiply",
    "/": "divide"
}

num1 = int(input("What is the first number?: "))
for symbols in operations: 
    print(symbols)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What is the second number?: "))
answer = 0
if operation_symbol == "+":
    answer = add(num1, num2)
elif operation_symbol == "-":
    answer = sub(num1, num2)
elif operation_symbol == "*":
    answer = multiply(num1, num2)
elif operation_symbol == "/":
    answer = divide(num1, num2)
or use this code down below

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}" )
"""

#answer key
#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    continue_cal = True

    while continue_cal:
        operation_symbol = input("Pick an operation: ") 
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            continue_cal = False
            #recursion happens when calling a function inside a function 
            calculator()

calculator()