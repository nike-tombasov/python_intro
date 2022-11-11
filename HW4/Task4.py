print("Homework 4. Task 4. Insert number for k. Creat new file with polynome", 
        "powered to k, where ratio numbers are random (from 0 to 100)")
print()

from random import randint
import datetime

k = int(input("Enter your power number k (can't be 0): "))
# k = 5
# poly_lst = []

if k:
    for i in range(1, 3):
        poly_lst = []
        file_name = "Polynome" + str(i) + ".txt"
        
        for j in reversed(range(k + 1)):
            ratio = randint(0,2)
            if ratio > 1:
                if j > 1:
                    poly_lst.append(str(ratio) + 'x^' + str(j))
                elif j:
                    poly_lst.append(str(ratio) + 'x')
                else:
                    poly_lst.append(str(ratio))
            elif ratio:
                if j > 1:
                    poly_lst.append('x^' + str(j))
                elif j:
                    poly_lst.append('x')
                else:
                    poly_lst.append(str(ratio))
        
        poly = " + ".join(poly_lst) + " = 0"
        print("Polynome " + str(i) + ":", poly)
        with open(file_name, 'w') as data:
            data.write(poly)
else: 
    print("Can't create polynome with power of 0")
