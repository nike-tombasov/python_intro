# nums = open("num.txt", 'r').read()
# print(nums)

# result = ((int(i), int(i) ** 2) for i in nums.split(' ') if int(i) % 2 == 0)
# print(result)

# print(nums.split(' '))

# 1
# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

from random import randint as rand
# import pprint

# nums = '1 2 3 4 5 6 8 9 10'

# lst = list(map(int, nums.split()))

# missed = list(lst[i] - 1 for i in range(1, len(lst)) if lst[i] - 1 != lst[i - 1])
# print(missed[0])

# for i in range(1, len(lst)):
#     if lst[i] - 1 != lst[i - 1]:
#         print(lst[i] - 1, "is missed")


# 2
# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# nums = [1, 5, 2, 3, 4, 6, 1, 7]

# # for i in range(10):
# #     nums.append(rand(1,11))
# print(nums)

# dct = []

# for k in range(len(nums)):
#     temp = k
#     lst = []
#     lst.append(nums[temp])
#     for i in range(temp, len(nums)):
#         if nums[i] > nums[temp]:
#             lst.append(nums[i])
#             temp = i
#     if len(lst) == 1:
#         lst.clear()
#     else:
#         dct.append(lst)
# print(dct)


# 3
# Напишите программу, удаляющую из текста все слова,
# в которых присутствуют все буквы "абв".

texted = "Ekd, lqp ajboc eowbc caodb qeab, bbc, pcba."
excluding = 'abc'
text_lst = texted.split()
print(text_lst)
for i in range(len(text_lst)):
    find = text_lst[i].lower()
    if excluding[0] in find and excluding[1] in find and excluding[2] in find:
        print(find)
        if ',' in find:
            text_lst[i] = ','
        elif '.' in find:
            text_lst[i] = '.'
        elif '!' in find:
            text_lst[i] = '!'
        elif '?' in find:
            text_lst[i] = '?'
        else:
            text_lst[i] = ''

print(text_lst)
result = " ".join(text_lst)
print(result)