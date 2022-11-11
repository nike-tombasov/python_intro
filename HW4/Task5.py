print("Homework 4. Task 5. Create file with sum of polynomes from existing files")
print()

def polynome_file (file_name): # Creating list of polynome
    poly = open(file_name, 'r').read()
    print(poly)
    poly = poly.replace(" = 0", "")
    poly = poly.split(' + ')
    return poly

def polynome_dict (polynome): # Creating dict from polynome
    poly_dict = {}
    for line in polynome:
        if line[-1] == 'x' and line[0] != 'x': 
            poly_dict[1] = [int(line[0:-1])]
        elif line[-1] == 'x' and line[0] == 'x':
            poly_dict[1] = [1]
        elif '^' in line:
            temp = line.find('^')
            if line[0] == 'x':
                poly_dict[int(line[temp + 1 :])] = [1]
            else:
                poly_dict[int(line[temp + 1 :])] = [int(line[: temp - 1])]
        elif 'x' not in line:
            poly_dict[0] = [int(line)]
    return poly_dict

poly_1 = polynome_file('Polynome1.txt')
poly_2 = polynome_file('Polynome2.txt')

poly_1 = polynome_dict(poly_1)
poly_2 = polynome_dict(poly_2)

for k, v in poly_2.items(): # Merging dicts
        if k in poly_1:
            poly_1[k].extend(v)
        else:
            poly_1[k] = v

poly_1 = dict(reversed(sorted(poly_1.items())))

poly_lst = [] # Summing polynomes from merged dicts
for j in poly_1.keys():
    ratio = sum(poly_1[j])
    
    if ratio > 1:
        if j > 1:
            poly_lst.append(str(ratio) + 'x^' + str(j))
        elif j:
            poly_lst.append(str(ratio) + 'x')
        else:
            poly_lst.append(str(ratio))
    elif ratio:
        if j > 1:
            poly_lst.append('x^' + str(j))
        elif j:
            poly_lst.append('x')
        else:
            poly_lst.append(str(ratio))
    
poly = " + ".join(poly_lst) + " = 0"
print("Sum of polynomes:", poly)
with open("Polynome_sum.txt", 'w') as data:
    data.write(poly)
