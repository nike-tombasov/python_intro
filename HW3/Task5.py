print("Homework 3. Task 3. Set list of real numbers.", 
        "Return difference between min and max fractional part of decimals from list")
print()

n = 10

lst = [1, 1]
fib1 = fib2 = 1
for i in range(2, n):
    fib1 = fib2
    fib2 = fib1 + fib2
    lst.append(fib2)

print(lst)