# Task 2

number2 = int(input("Enter your number: "))
array2 = [0]

if number2 != 0:
    array2[0] = 1
    for i in range(2, abs(number2) + 1):
        array2.append(array2[i-2]*i)
print("List of multiplying from 1 to entered number:", array2)
