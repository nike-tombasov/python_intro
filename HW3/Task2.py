print("Homework 3. Task 2. Set random list of numbers.", 
        "Return multiplication of numbers pair", 
        "where pairs are taken specularly starting from first and last postitions.")

from random import randint as r

lst, lst_lenght, multiplication = [], 7, 1
for i in range(lst_lenght):
    lst.append(r(0, 10))
print("Random list of numbers:", lst)

