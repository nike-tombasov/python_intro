# 1. Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

from re import X


nums = '1 0 8 16 7 3'
lst = list(map(int, nums.split(" ")))
# lst = [int(i) for i in nums.split(" ")]

print(lst)
print(min(lst))
print(max(lst))

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python

a = 2
b = 4
c = 2
x1 = None
x2 = None
discrim = b**2 - 4 * a * c

if a == 0:
    print("No solutions")
elif discrim > 0:
    x1 = (-b + discrim**0.5) / (2 * a)
    x2 = (-b - discrim**0.5) / (2 * a)
    print("Two roots:",)
    print("1) x =", rccound(x1))
    print("2) x =", round(x2))
elif discrim == 0:
    x1 = (-b + discrim**0.5) / (2 * a)
    print("One root:",)
    print("x =", round(x1))
else:
    print("No roots.")


# 3. Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

num_A = 115
num_B = 50
num_max = max(num_A, num_B)
num_min = min(num_A, num_B)
gcd = None
lcm = None
temp = None
temp2 = None


if num_max % num_min == 0:
    gcd = num_min
else:
    gcd = num_max % num_min
    temp = gcd
    temp2 = num_min
    while temp > 0:
        gcd = temp
        temp = temp2 % temp
        temp2 = gcd

lcm = round(abs(num_A * num_B) / gcd)

print(f"GCD({num_A}; {num_B}):", gcd)
print(f"LCM({num_A}; {num_B}):", lcm)

#option2

while True:
    if num_max % num_A == 0 and num_max % num_B == 0:
        lcm = num_max
        break
    num_max += 1
print(lcm)

#GCD
def gcd(x, y):
    if y < x: x, y = y, x
    if y == 0: return x
    return gcd(y, x % y)


# DZ
# 2. Любое составное число имеет множитель, 
# который не превосходит корень из этого числа. 
# 3. Вывести уникальные числа. 
# 4. Сформировать полином (многочлен)
