# Task 3 

number3 = int(input("Enter your number: "))
array3 = []
sum3 = 0

if number3 != 0:
    for i in range(1, number3 + 1):
        array3.append((1 + 1 / i) ** i) 
        sum3 += array3[i - 1]
else: array3.append(0)

print(f"Sum of sequence (1 + 1 / n) ** n for n = {number3} is -", sum3)
