# I
a = 4
b = 16

if b == a ** 2 or a == b ** 2:
    print("Yes")
else:
    print("No")

# II
a = 4
b = 5
c = 2
d = 3
e = 1

temp = a

for i in a, b, c, d, e:
    if i > temp:
        temp = i
print(temp)


# III
q = -3
a = abs(q)

for i in range(-a, a + 1):
    print(i, end=", ")
    
print()
# print(*range(-(n:= abs(-5)),n+1), sep = ", ")


# IV
a = "123"
b = int(abs(float(a)) * 10 % 10)

#print(b if a - int(a) != 0 else "No")


#for i in range(len(a)):
#    if a[i] == ".":
#        print(a[i+1])


#print(str(float(a))[str(float(a)).find('.') + 1])
print(str(float(a)).split('.')[1][0])

# V
a = 75

if ((a % 5 == 0) and (a % 10 == 0) or (a % 15 == 0)) and a % 30 != 0:
    print("Yes")
else: 
    print("No")
