print("""Homework 6. Task 1. Make calculator that takes string of input data.
        Use +, -, *, / operations only with logical priority. 
        Additionaly include () operations with appropriate logical priority""", end="\n\n")

# expression = input("Enter your expression: ")
expression = 'A500-1000/5*10.5'

nums = '' # "1 -2 3"
operats = '' # "+*"
check = '0123456789/*-+.' # Input filter

opers = { # Functions
        '/': lambda x,y: x / y,
        '*': lambda x,y: x * y,
        '+': lambda x,y: x + y}


for i in expression: # Split input to nums and operations
    if i not in check:
        pass
    elif i.isdigit() or i == '.':
        nums += i
    elif i == '-':
        nums += ' ' + i
        operats += '+'
    else:
        nums += ' '
        operats += i

nums_lst = list(map(float, nums.split())) # Converting nums into list
op_lst = list(operats) # Converting operations into list

while len(nums_lst) > 1: # Calculation
    for o in "/*+":
        if o in op_lst:
            i = op_lst.index(o)
            nums_lst[i] = opers[o](nums_lst[i], nums_lst[i + 1])
            del nums_lst[i + 1]
            op_lst.remove(o)

print(nums_lst[0])
 