# Task 4 

from random import randint

number4 = abs(int(input("Enter your number - length for a list: ")))
array4 = []
multiplication4 = 1

if number4 != 0: 
    for i in range(number4):
        array4.append(randint(-number4, number4))
    print(array4)
    print()

    file4 = open("indexes.txt", 'r')
    file_min = 100
    for line in file4:
        if int(line) < file_min: file_min = int(line)

        if int(line) < number4:
            multiplication4 *= array4[int(line)]
            print(f"For file's index {int(line)} number is:", array4[int(line)])
    file4.close()

    if number4 - 1 < file_min:
        print("Multiplication of numbers by file's indexes:", 0)
    else:
        print()
        print("Multiplication of numbers by file's indexes:", multiplication4)
else: 
    print("Entered number is 0 - couldn't generate list and make multiplication")
