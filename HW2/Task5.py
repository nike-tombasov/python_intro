# Task 5 

from random import randint

array5 = ["That", "things", "we", "made", "!"]

# array5 = []
# num5 = int(input("Enter your number - length for a random list: "))
# for i in range(num5):
#     array5.append(randint(-num5, num5))

print("Input list to mix:", array5)

for i in range(len(array5)):
    rand_num = randint(0, len(array5) - 1)
    temp = array5[i]
    array5[i] = array5[rand_num]
    array5[rand_num] = temp

print("List after mixing:", array5)
