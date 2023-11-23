import random
def play_game(computer,player):
    if computer == player:
        return 0
    elif player == 0 and computer == 1:
        return 1
    elif player == 1 and computer == 2:
        return 1
    elif player == 2 and computer == 0:
        return 1
    else:
        return -1

player =int(input("enter 0 : Snake , 1:Water , 2:Gun \n"))
computer=random.randint(0,2)
print("Computer :",computer)
print("You :",player)
score =play_game(computer,player)
if score == 0:
    print("DRAW")
elif score == 1:
    print("YOU WIN")
else:
    print("YOU LOSE")