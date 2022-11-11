print("Homework 4. Task 3. Make list of unique numbers from given list")
print()

lst = [5, 5 , 12, 0, 1, 12, 6, 5, 3]
result_lst = []

for i in lst:
    if lst.count(i) < 2:
        result_lst.append(i)

print("Given list of numbers:", lst)
print("List of unique numbers from given list:", result_lst)
result_lst.sort()
print("Sorted list of unique numbers from given list:", result_lst)