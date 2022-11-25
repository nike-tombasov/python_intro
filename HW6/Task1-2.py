print("""Homework 6. Task 1. Make calculator that takes string of input data.
        Use +, -, *, / operations only with logical priority. 
        Additionaly include () operations with appropriate logical priority""", end="\n\n")

import sys

# expression = input("Enter your expression (only +,-,*,/ and numbers): ")
# expression = 'A500-411.12/5*10+600/6fefqwef+8.8'
# expression = '-3'
# expression = '(3+3)+((3-3)+2)'  
expression = '(1+2)*3'

ops_f = {  # Functions
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y}
filter = '0123456789/*-+.()'  # Input filtration

cleared_expression = []  # Output visual
for i in expression:
    if i in filter:
        cleared_expression.append(i)
    elif i == ',':
        cleared_expression.append('.')

def convert_expression(current_input):
    nums = ''
    operations = ''

    for i in current_input:  # Split input to nums and operations
        if i not in filter:
            pass
        elif i.isdigit() or i == '.':  # Digits
            nums += i
        elif i == '-':  # Negative for digits
            nums += ' ' + i
            operations += '+'
        else:  # Operations
            nums += ' '
            operations += i

    nums_lst = list(map(float, nums.split()))  # Converting nums into list
    ops_lst = list(operations)  # Converting operations into list

    return nums_lst, ops_lst


def calculation(input):
    if '(' in input: # Recursion 
        before_i = input.index('(')
        after_i = input.rindex(')')
        return calculation(input[:before_i] + calculation(input[before_i + 1:after_i]) + input[after_i + 1:])

    nums_lst, ops_lst = convert_expression(input) # Convertation

    if len(ops_lst) == 0: # Main exit
        return input

    for op in ops_f:  # Operation
        for _ in range(ops_lst.count(op)):
            i = ops_lst.index(op)
            if op == '/' and nums_lst[i + 1] == 0:
                sys.exit("Dividing by zero. Aborting calculation.")
            nums_lst[i] = ops_f[op](nums_lst[i], nums_lst[i + 1])
            del nums_lst[i + 1]
            del ops_lst[i]

    return str(nums_lst[i])


result = float(calculation(expression))
if result == int(result):  # Clearing float .0
    result = int(result)

# Output
print('Calculation:')
print(''.join(cleared_expression), "=", round(result, 12))
