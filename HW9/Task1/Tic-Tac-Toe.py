from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe")
field = []
player = ('X', '0')
i = 0
step = 1
fld_lst = [['', '', ''], ['', '', ''], ['', '', '']]


def move(row, column):
    global step
    global i

    if field[row][column]['text'] == ' ':
        field[row][column]['text'] = player[i]
        fld_lst[row][column] = player[i]
        
        win_check(row, column, step, i)
        if i: 
            i = 0
        else: 
            i = 1
        step += 1
    else:
        field[row][column]['text'] = field[row][column]['text']


def win_check(row, column, step, i):
    colmns = list(zip(fld_lst[0], fld_lst[1], fld_lst[2]))
    diags = [[fld_lst[0][0], fld_lst[1][1], fld_lst[2][2]],
             [fld_lst[0][2], fld_lst[1][1], fld_lst[2][0]]]
    if (row == 1 and column == 1) or (row != 1 and column != 1):  # check both diagonals
        if diags[0].count(player[i]) == 3 or diags[1].count(player[i]) == 3:
            messagebox.showinfo(title='Game Over!', message=f'{player[i]} wins!!!')
    elif fld_lst[row].count(player[i]) == 3:  # check current line
        messagebox.showinfo(title='Game Over!', message=f'{player[i]} wins!!!')
    elif colmns[column].count(player[i]) == 3:  # check current column
        messagebox.showinfo(title='Game Over!', message=f'{player[i]} wins!!!')
    elif step == 9:
        messagebox.showinfo(title='Game Over!', message='Draw! Nobody wins.')


for row in range(3): # Field creation
    line = []
    for column in range(3):
        button = Button(root, text=' ', height=4, width=9,
            command=lambda row=row, column=column: move(row, column))
        button.grid(row=row, column=column, sticky=NSEW)
        line.append(button)
    field.append(line)

root.mainloop()




def players_move(name, symbol, step):
    print(f"Step {step}. {name}, your turn")
    check = 1
    x, y = 0, 0
    while check:
        move = (int(input("Enter line (1-3): ")) - 1,
                int(input("Enter column (1-3):")) - 1)
        x, y = move[0], move[1]
        if not (0 <= x <= 2) or not (0 <= y <= 2):
            print(f"Position {(x+1, y+1)} out of field range. Try again.")
        elif field[x][y] != '_' and field[x][y] != ' ':
            print(f"Position {(x+1, y+1)} is not empty. Try again.")
        else:
            check = 0

    field[x][y] = symbol

    # Check for game end
    colmns = list(zip(field[0], field[1], field[2]))
    diags = [[field[0][0], field[1][1], field[2][2]],
             [field[0][2], field[1][1], field[2][0]]]
    if (x == 1 and y == 1) or (x != 1 and y != 1):  # check both diagonals
        if diags[0].count(diags[0][0]) == 3 or diags[1].count(diags[1][0]) == 3:
            print(f"{name} wins!!!")
            exit()
    if field[x].count(field[x][0]) == len(field[x]):  # check current line
        print(f"{name} wins!!!")
        exit()
    if colmns[y].count(colmns[y][0]) == 3:  # check current column
        print(f"{name} wins!!!")
        exit()
    if step == 9:
        print("Draw! Nobody wins.")
        exit()
    
    step += 1
    return step