print("Homework 5. Task 2. Make programm that helps win in a game person vs person,", 
        "where first player take candies and win in the end. Max for one move",
        " - 28 candies. Total in the game - 2021 candies. First player is",
        "chosen by the drowing lots. Wins the last moved player.")
print("First PC autowinner vs PC game version")
print()

from random import randint as r
from time import sleep

def bot(total, max, name, cache):
    print(f"{name} thinking...")
    if total > max:
        player = r(0, max)
    else:
        player = r(0, total)
    sleep(2)
    print(f"{name} takes {player} candies")
    if total - player == 0:
        print("0 candies left.") 
        print(f"{name} wins and takes all candies!!!")
        exit()
    total -= player
    cache += player
    sleep(1)
    print("Candies left:", total)
    sleep(1)
    return total, cache

def bot_winner(total, max, name, cache):
    print(f"{name} thinking...")
    player = total % (max + 1)
    sleep(2)
    print(f"{name} takes {player} candies")
    if total - player == 0:
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

name_1 = "PC python bot 1"
name_2 = "PC python bot 2"


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
    print(f"Move {move}.")
    sleep(1)
    if lottery:
        candies, player_1 = bot_winner(total=candies, max=max, name=name_1, cache=player_1)
        candies, player_2 = bot(total=candies, max=max, name=name_2, cache=player_2)
    else:
        candies, player_2 = bot_winner(total=candies, max=max, name=name_2, cache=player_2)
        candies, player_1 = bot(total=candies, max=max, name=name_1, cache=player_1)
    move += 1
    sleep(1)
    print(f"{name_1} took {player_1} candies")
    print(f"{name_2} took {player_2} candies")
    sleep(1)
    print()
