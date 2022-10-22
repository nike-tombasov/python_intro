# Практика
# 1. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

# 2. Напишите программу, которая определит
# позицию второго вхождения строки в списке либо сообщит, что её нет.

# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


# 1
# lst = ["qwerty", "a90sd", "zxc", "qw5e", "ertqwe"]
# num = 905

# print(f"Return is {num} in:", lst)

# for i in lst:
#     if str(num) in i:
#         print(True)
#         break
# else: print(False)

# print(True if str(num) in ' '.join(lst) else False) # 2-nd option


# 2
lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
searching = "qwe"

if lst.count(searching) >= 2:
    count = 0 
    for i in range(len(lst)):
        if lst[i] == searching:
            if count == 1:
                print(i)
                break
            count += 1
else: 
    print(None)

#2-nd option
if lst.count(searching) >= 2:
    ind = lst[lst.index(searching) + 1:].index(searching) + 1
    print(ind)
else: 
    print(None)

#3-nd option
print(lst[lst.index(searching) + 1:].index(searching) + 1 if lst.count(searching) >= 2 else None)