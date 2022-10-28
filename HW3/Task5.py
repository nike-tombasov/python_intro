print("Homework 3. Task 3. Set list of real numbers.", 
        "Return difference between min and max fractional part of decimals from list")
print()

n = 10

lst = [1]
fib1, fib2 = 0, 1
fib = 0
for i in range(1, n):
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    lst.append(fib)

print(lst)

# F(-n)=(-1)^{n+1} *  F(n)