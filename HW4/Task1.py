print("Homework 4. Task 1. Option 1. Round up float number to the power of", 
        "inserted number formed as 10 ** (-1) <= 1 <= 10 ** (-10)")
print()

from random import uniform
from decimal import Decimal

# d = input("Enter your dot number in range 10 ** (-1) <= 1 <= 10 ** (-10): ")
d = Decimal("0.001")
num = uniform(0, 100)

print("Float number to round up:", num)
print(f"Rounded number:", round(num, len(str(d).split(".")[1])))