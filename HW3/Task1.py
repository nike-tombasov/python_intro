print("Homework 3. Task 1. Set random list of numbers.", 
        "Return sum of every number in odd positions.")

from random import randint as r

lst, sum_odd = [], 0
for i in range(10):
    lst.append(r(0, 10))
print("Random list of numbers:", lst)

for i in range(len(lst)):
    if i % 2 != 0:
        sum_odd += lst[i]
print("Sum of every number in odd positions:", sum_odd)
