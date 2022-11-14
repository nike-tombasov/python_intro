print("""Homework 6. Task 1. Make calculator that takes string of input data.
        Use +, -, *, / operations only with logical priority. 
        Additionaly include () operations with appropriate logical priority""", end="\n\n")


#  2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
#  1+2*3 => 7; (1+2)*3 => 9;

#expression = input("Enter your expression: ")
expression = '5+25/5-2*2'
plus_lst = expression.split('+')
sum = 0
for i in range(len(plus_lst)): # Main loop
    if '-' in str(plus_lst[i]): # Minuses check and loop
        minus_lst = plus_lst[i].split('-')
        minus = 0
        for j in range(len(minus_lst)):
            if '*' in str(minus_lst[j]): # Multipl check and loop
                mult_lst = minus_lst[j].split('*')
                mult = 1
                for k in range(len(mult_lst)):
                    if '/' in str(mult_lst[k]): # Divid check and loop
                        divid_lst = mult_lst[k].split('/')
                        for l in range(len(divid_lst)-1):
                            if int(divid_lst[l+1]) == 0:
                                print("Division by zero. Wrong expression.")
                            divid = int(divid_lst[l]) / int(divid_lst[l+1])
                        mult_lst[k] = divid
                    mult *= int(mult_lst[k])
                minus_lst[j] = mult
            if '/' in str(minus_lst[j]): # Divid check and loop
                divid_lst = minus_lst[j].split('/')
                for l in range(len(divid_lst)-1):
                    if int(divid_lst[l+1]) == 0:
                        print("Division by zero. Wrong expression.")
                    divid = int(divid_lst[l]) / int(divid_lst[l+1])
                minus_lst[j] = divid
            minus -= int(minus_lst[j])
        plus_lst[i] = minus
    if '*' in str(plus_lst[i]): # Multipl check and loop
        mult_lst = plus_lst[i].split('*')
        mult = 1
        for k in range(len(mult_lst)):
            if '/' in mult_lst[k]:
                divid_lst = mult_lst[k].split('/')
                for l in range(len(divid_lst)-1):
                    if int(divid_lst[l+1]) == 0:
                        print("Division by zero. Wrong expression.")
                    divid = int(divid_lst[l]) / int(divid_lst[l+1])
            mult *= int(mult_lst[k])
        plus_lst[i] = mult
    if '/' in str(plus_lst[i]): # Multipl check and loop
        divid_lst = plus_lst[i].split('/')
        for l in range(len(divid_lst)-1):
            if int(divid_lst[l+1]) == 0:
                print("Division by zero. Wrong expression.")
            divid = int(divid_lst[l]) / int(divid_lst[l+1])
        plus_lst[i] = divid
    sum += int(plus_lst[i])
    print(i, " => ", sum)

print(sum)
