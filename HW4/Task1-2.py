print("Homework 4. Task 1. Option 2. Round up float number to the power of", 
        "inserted number formed as 10 ** (-1) <= 1 <= 10 ** (-10)")
print()

from random import uniform
from decimal import Decimal

d = Decimal(input("Enter your dot number in range 10 ** (-1) <= 1 <= 10 ** (-10): "))
num = Decimal(str(uniform(0, 100)))

print("Float number to round up:", num)
print(f"Rounded number:", num.quantize(d))