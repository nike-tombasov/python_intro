print("Homework 3. Task 5. From inserted number set list of Fibonacci numbers", 
        "also including negative sequence.")
print()

n = abs(int(input("Enter your number for Fibonacci sequence: ")))
lst, positiv_lst = [-1], [1]
fib, fib1, fib2 = 0, 0, 1

for i in range(1, n):
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    lst.append(-fib)
    positiv_lst.append(fib)

lst.reverse()
lst.append(0)
lst += positiv_lst

print("Fibonacci and negafibonacci sequence: ", lst)
