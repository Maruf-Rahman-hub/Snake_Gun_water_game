import random
def gameWin(computer , player):
    if computer == player:
        return None
    elif computer == "s":
        if player == "w":
            return False
        elif player == "g":
            return True 
    elif computer == "w":
        if player == "g":
            return False
        elif player == "s":
            return True   
    elif computer == "g":
        if player == "s":
            return False
        elif player == "w":
            return True               

print("Computers turn : Snake(s) , Water(w) , or Gun(g) ?")
randomNo = random.randint(1 , 3)
if randomNo == 1:
    computer = "s"
elif randomNo == 2:
    computer = "w"
elif randomNo == 3:
    computer = "g"    
player = input(" players turn : Snake(s) , Water(w) , or Gun(g) ? \n")

i = gameWin(computer , player)
print(f"Computer Choose {computer}")
print(f"Player Choose {player}")

if i == None:
    print("The game is tie")
elif i :
    print("Player wins")
else:
    print("Player lost")        