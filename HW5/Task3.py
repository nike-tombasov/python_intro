print("Homework 5. Task 4. Realize Tic-Tac-Toe game")
print()

from random import randint as r
from pprint import pprint

def print_f(field):
    for i in field:
        print(*i, sep="|")

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
    print_f(field)
    print()

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

field = [["_", "_", "_"], ["_", "_", "_"], [" ", " ", " "]]
print_f(field)
print()
lottery = r(0, 1)  # Who is first


# Naming
if (x := input("Player 1, enter your name or press Enter: ")) != '':
    name_1 = x
else:
    name_1 = "Player 1"
if (x := input("Player 2, enter your name or press Enter: ")) != '':
    name_2 = x
else:
    name_2 = "Player 2"

# Lotter
if lottery:
    print(f"{name_1} plays first")
else:
    print(f"{name_2} plays first")
print()

step = 1
while True:
    # print(f"Step {step}.", end=' ')
    if lottery:
        step = players_move(name_1, 'X', step=step)
        step = players_move(name_2, 'O', step=step)
    else:
        step = players_move(name_2, 'X', step=step)
        step = players_move(name_1, 'O', step=step)
    # move += 1
