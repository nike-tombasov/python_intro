print("Homework 3. Task 2. Set random list of numbers.", 
        "Return multiplication of numbers pair", 
        "where pairs are taken specularly starting from first and last postitions.")
print()

from random import randint as r

lst, result_lst, lst_lenght = [], [], 10

for i in range(lst_lenght):
    lst.append(r(0, 10))
print("Random list of numbers:", lst)

if len(lst) % 2 == 0:
    for i in range(len(lst) // 2):
        result_lst.append(lst[i]*lst[-1 - i])
else:
    for i in range(len(lst) // 2 + 1):
        result_lst.append(lst[i]*lst[-1 - i])

print(result_lst)


# for i in range((len(lst) + 1) // 2):
#     result_lst.append(lst[i]*lst[-1 - i])

# lst = [r(0, 10) for _ in range(lst_lenght)]