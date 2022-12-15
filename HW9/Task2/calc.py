import sys

ops_f = {  # Functions
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y}
filter = '0123456789/*-+.()'  # Input filtration base

# expression = input("Enter your expression (only +,-,*,/ and numbers): ")

# async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     input = update.message.text
#     result = float(calculation(input.split()[1:]))
#     if result == int(result):  # Clearing float .0
#         result = int(result)
#     await update.message.reply_text(''.join(clearing_expression(input)), "=", round(result, 12))


def clearing_expression(expression):    
    cleared_expression = []  # Output visual 
    for i in expression:
        if i in filter:
            cleared_expression.append(i)
        elif i == ',':
            cleared_expression.append('.')
    return cleared_expression


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


# print(calculation('2+2'))


# Output
# print('Calculation:')
# print(''.join(cleared_expression), "=", round(result, 12))