print("Homework 5. Task 2. Make programm that helps win in a game person vs person,", 
        "where first player take candies and win in the end. Max for one move",
        " - 28 candies. Total in the game - 2021 candies. First player is",
        "chosen by the drowing lots. Wins the last moved player.")
print("Full interactive game version")
print()

from random import randint as r
from time import sleep

def players_move(total, max, name, cache):
    player = max + 1
    while player > max or player < 0:
        player = int(input(f"{name}, your move. Take candies (28 max): "))
        if player > max or player < 0:
            print(f"Wrong number of candies. {name}, try again")
        elif total - player < 0:
            print(f"Not enought candies. {name}, try again")
            player = max + 1
        elif total - player == 0:
            print("0 candies left.") 
            print(f"{name} wins and takes all candies!!!")
            exit()
    total -= player
    cache += player
    sleep(1)
    print("Candies left:", total)
    sleep(1)
    return total, cache

candies = 50 #2021
max = 28
player_1 = 0
player_2 = 0
lottery = r(0, 1) #Who is first

if (x := input("Player 1, enter your name or press Enter: ")) != '': 
    name_1 = x
else: 
    name_1 = "Player 1"
if (x := input("Player 2, enter your name or press Enter: ")) != '': 
    name_2 = x
else: 
    name_2 = "Player 2"


sleep(1)
print("Total condies: ", candies)
sleep(1)
print(f"{name_1} vs {name_2}")
sleep(2)

if lottery:
    print(f"{name_1} plays first")
else: 
    print(f"{name_2} plays first")
print()

move = 1
while True:
    sleep(1)
    print(f"Move {move}.")
    if lottery:
        candies, player_1 = players_move(total=candies, max=max, name=name_1, cache=player_1)
        candies, player_2 = players_move(total=candies, max=max, name=name_2, cache=player_2)
    else:
        candies, player_2 = players_move(total=candies, max=max, name=name_2, cache=player_2)
        candies, player_1 = players_move(total=candies, max=max, name=name_1, cache=player_1)
    move += 1
    sleep(1)
    print(f"{name_1} took {player_1} candies")
    print(f"{name_2} took {player_2} candies")
    sleep(1)
    print()
