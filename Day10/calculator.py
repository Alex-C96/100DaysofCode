# Calculator Program
# Alexander Clarke
# 12/25/2021

# import artwork
from art import logo
# import only system from os
from os import system, name

# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Calculator functions 
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print(logo)

operations = {'+':add, '-':subtract, '*':multiply, '/':divide}


def calculator():
    should_continue = True
    num1 = float(input('What\'s the first number?: '))
    # display operation choices
    for operator in operations:
        print(operator)

    while(should_continue):
        symbol = input('Pick an operation from the line above: ')
        num2 = float(input('What\'s the next number?: '))
        # get the function from the dictionary, operations
        function = operations[symbol]
        try:
            result = function(num1, num2)
            print(f'{num1} {symbol} {num2} = {result}')
            cont = input("Type 'y' to continue calculating with {result} or type 'n' to start a new calculation.: ")
        except ZeroDivisionError as err:
            print('Handling invalid input:', err)
            cont = 'n'
        if cont == 'y':
            num1 = result
        else:
            should_continue = False
            calculator()

calculator()
        
    
    
