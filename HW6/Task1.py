print("""Homework 6. Task 1. Make calculator that takes string of input data.
        Use +, -, *, / operations only with logical priority. 
        Additionaly include () operations with appropriate logical priority""", end="\n\n")

import sys

# expression = input("Enter your expression (only +,-,*,/ and numbers): ")
expression = 'A500-411.12/5*10+600/6fefqwef+8.8'

nums = ''
operations = ''
cleared_expression = [] # Output visual
check = '0123456789/*-+.'  # Input filtration
ops_f = {  # Functions
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y}

for i in expression:  # Split input to nums and operations
    if i not in check:  # Filter
        pass
    elif i.isdigit() or i == '.':  # Digits
        nums += i
        cleared_expression.append(i)
    elif i == '-':  # Negative for digits
        nums += ' ' + i
        operations += '+'
        cleared_expression.append(i)
    else:  # Operations
        nums += ' '
        operations += i
        cleared_expression.append(i)

nums_lst = list(map(float, nums.split()))  # Converting nums into list
op_lst = list(operations)  # Converting operations into list

for op in ops_f:  # Calculation
    for _ in range(op_lst.count(op)):
        i = op_lst.index(op)
        if op == '/' and nums_lst[i + 1] == 0:
            sys.exit("Dividing by zero. Aborting calculation.")
        nums_lst[i] = ops_f[op](nums_lst[i], nums_lst[i + 1])
        del nums_lst[i + 1]
        del op_lst[i]

if nums_lst[0] == int(nums_lst[0]):  # Clearing float .0
    nums_lst[0] = int(nums_lst[0])

# Output
print('Calculation:')
print(''.join(cleared_expression), "=", round(nums_lst[0], 12))
