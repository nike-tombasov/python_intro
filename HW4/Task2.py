print("Homework 4. Task 2. Make list of simple multipliers", 
        "of inserted number.")
print()

num = int(input("Enter your number: "))
# num = 1084
temp, multipl, multipl_lst = num, 2, []

while multipl <= temp:
    if temp % multipl == 0:
        multipl_lst.append(multipl)
        temp //= multipl
        multipl = 2
    else: 
        multipl += 1

print(multipl_lst)
