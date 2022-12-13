import calc

input = '/calculate 2+2'
print(*input.split()[1:])

result = float(calc.calculation(*input.split()[1:]))
if result == int(result):  # Clearing float .0
    result = int(result)
output = ''.join(calc.clearing_expression(*input.split()[1:])), "=", round(result, 12)
output2 = ''.join(map(str, output))
print(type(output2))
print(str(output))
