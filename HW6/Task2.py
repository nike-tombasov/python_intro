print("""Homework 6. Task 2. From given list return list with unique elements,
        list with doubling elements, with list without duplicates""", end="\n\n")

import time

start = time.time()

lst = [1, 2, 3, 5, 1, 5, 3, 10, 5, 5, 12, 0, 1, 12, 6, 5, 3]
unique_lst = list(i for i in set(lst) if lst.count(i) == 1)
doubling_lst = list(set(lst) - set(unique_lst))
clean_lst = list(set(lst))

# for i in set(lst):
#     if lst.count(i) == 1:
#         unique_lst.append(i)
#     else:
#         doubling_lst.append(i)

print("Given list of element:", lst)
print("List of unique elements from given list:", unique_lst)
print("List of doubling elements from given list:", doubling_lst)
print("List without duplicates:", clean_lst)
print("Spent time:", (time.time() - start) * 1000)