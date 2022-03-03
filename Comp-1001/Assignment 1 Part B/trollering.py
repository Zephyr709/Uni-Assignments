##
# This program plays a game of troller ring against a user
# and computes and outputs the winner
##

#Imported functions
from random import randint

# Variables
playerName = input("Please enter your first name: ")

# Generates the random numbers between 10-20 for troll plate num
tpn1,tpn2,tpn3 = randint(10,20), randint(10,20), randint(10,20)
tpnTotal = tpn1+tpn2+tpn3
# Generates the random numbers between 20-24 for troll plate image
tpi1,tpi2,tpi3 = randint(20,24), randint(20,24), randint(20,24)

# Generates the random numbers between 1-6 for troll plate pod
tpp1,tpp2,tpp3 = randint(1,6), randint(1,6), randint(1,6)

invisPlayer = randint(120,150) #generates a score for the invisible player

if (tpn1 + tpn2 + tpn3) >= 50 or ((tpi1 == tpi2) and (tpp1+tpp2+tpp3) >= 12):
   
    playerScore = (tpn1+tpn2+tpn3)*2 + tpp1+tpp2+tpp3 + tpi1+tpi2+tpi3
    
    print(playerName, "you earned", playerScore, "points")
    print("Your opponent earned", invisPlayer, "points")
    
    if invisPlayer > playerScore:
        print("Sorry", playerName, "you have lost the game to your opponent.")
    elif invisPlayer == playerScore:
        print(playerName, "you have tied with your opponent.")
    elif invisPlayer < playerScore:
        print(playerName, "congratulations you are the winner of the game.")

else:
    playerScore = (tpn1+tpn2+tpn3 + tpp1+tpp2+tpp3 + tpi1+tpi2+tpi3)
    
    print(playerName, "you earned", playerScore, "points")
    print("Your oppent earned", invisPlayer, "points")
    
    if invisPlayer > playerScore:
        print("Sorry", playerName, "you have lost the game to your opponent.")
    elif invisPlayer == playerScore:
        print(playerName, "you have tied with your opponent.")
    elif invisPlayer < playerScore:
        print(playerName, "congratulations you are the winner of the game.")
    