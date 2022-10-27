print("Homework 3. Task 3. Set list of real numbers.", 
        "Return difference between min and max fractional part of decimals from list")
print()

from random import uniform

lst, lst_lenght = [], 5
# lst = [1.1, 1.2, 3.1, 5, 10.01]

for i in range(lst_lenght):
    lst.append(round(uniform(0, 10), 2))
print("Random list of real numbers:", lst)

for i in range(len(lst)):
    lst[i] = round(lst[i] % 1, 5)

print("Option #1. Difference between min and max fractional part:", max(lst) - min(lst))


# for i in range(len(lst)):
#     lst[i] = round(lst[i] - lst[i] // 1, 5)

# print("Option #2. Difference between min and max fractional part:", max(lst) - min(lst))