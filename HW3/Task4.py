print("Homework 3. Task 4. Make decimal to binary convertor.")
print()

# Option 1

# decim = 45
# binar = "{0:b}".format(decim)
# print(binar)

# Option 2

decim, lst, binar = abs(int(input("Enter your integer decimal: "))), [], 0

while decim != 0:
    lst.append(decim % 2)
    decim //= 2

lst.reverse()

if len(lst) == 0: 
    print(0)
else:
    binar = "".join(map(str, lst))
    print(binar)