# Task 1.

number1 = float(input("Enter your real number (for float only use '.'): "))

if type(number1) == float or type(number1) == int:
    str1 = str(number1) 
    sum1 = 0
    for i in str1:
        if i != "." and i != "-":
            sum1 += int(i)
    print("Sum of every digit in your number - ", sum1)
else: print("Insered value is not real number. Try again.")
