##
# This program simulates two games from Centauros; Cornhole and Guessing medals
#
##

# Needed libraries 
from random import randint

#Functions
def displayMenu():#displays the menu, gets input from user, and validates it
    print("Choose 1 or 2 to play one of the following games, or 3 to quit playing \n"
          + "1. Cornhole \n" + "2. Guessing Medals \n" + "3. Quit")
    choice = input("Enter your choice: ")
    
    while choice != "1" and choice != "2" and choice != "3":#validates input
        print("Please enter a valid choice (1,2,3)")
        print("Choose 1 or 2 to play one of the following games, or 3 to quit playing \n"
              + "1. Cornhole \n" + "2. Guessing Medals \n" + "3. Quit")
        choice = input("Enter your choice: ")
    
    if choice == "3":
        print("Goodbye. Hope you enjoyed playing!")
    
    return choice
    
def cornhole():#Runs the game of cornhole
    playerPts = 0
    print("You are playing Cornhole!")
    for i in range(4):#plays the game 4 times,validates user input, and prints the results
        print("\n", "Your playing round", i+1)
        colour = input("Enter the colour of the baggie you are throwing "
                   + "(red/yellow/blue/green) : ").lower()
        while colour!="red" and colour!="yellow" and colour!="blue" and colour!="green":
            colour = input("Please enter a valid selection "
                       + "(red/yellow/blue/green) : ").lower()
       
        playerPts += computeTossPoints(colour)
    
    printWinner(playerPts)
    
def computeTossPoints(colour): #Calculates points and returns the outcome of the toss
    landLoc = randint(0,4)
    
    if landLoc == 0:
        statement = "outside the points area!"
        playerPts = 0
    elif landLoc == 1:
        statement = "in the hole."
        if colour != "red":
            playerPts = 8
        else: 
            playerPts = 10
    elif landLoc == 2:
        statement = "on the yellow ring."
        if colour != "yellow":
            playerPts = 3
        else:
            playerPts = 6
    elif landLoc == 3:
         statement = "on the blue ring."
         if colour != "blue":
             playerPts = 2
         else:
             playerPts = 4
    elif landLoc == 4:
        statement = "on the green ring."
        if colour != "green":
            playerPts = 1
        else:
            playerPts = 2
    
    
    cornholeResults(colour, statement)
    print("You scored", playerPts, "points this round!")
    return playerPts

def cornholeResults(colour,statement): # Constructs the output statement in cornhole
    print(colour,"bag lands", statement)
    
def printWinner(playerPts):#Generates computer score then prints the winner
    compPts = randint(0,34)
    print("\n", "You scored", playerPts, "points. The computer scored", compPts, "points.")
    if playerPts < compPts:
        print("The computer won the game by", (compPts-playerPts), "points.")
        return
    if playerPts == compPts:
        print("The game was a tie!")
        return
    if playerPts > compPts:
        print("Congratulations! You won the game by", (playerPts-compPts), "points.")
        return
    
def guessMedals():#Runs the game of Guess medals
    flag = True
    print("You are playing Guess Medals!")
    guess = input("Please enter your guess as a number between 0 and 200: ")
    print("\n")
    while flag:#This loop checks validity of input and prompts user if incorrect
        if guess.isdigit():
            guess = int(guess)
            if guess >= 0 and guess <=200:
                num = randint(50,150)#generates random number
                difference = abs(guess - num)#Takes the absoulute value of the difference
                if difference >= 50:
                    medal ="a Bronze medal."
                    gMedalsResults(medal,difference)
                    print("The number to guess was:", num)
                    return
                if difference >= 20:
                    medal = "a Silver medal."
                    gMedalsResults(medal,difference)
                    print("The number to guess was:", num)
                    return
                if difference >= 5:
                    medal = "a Gold medal."
                    gMedalsResults(medal,difference)
                    print("The number to guess was:", num)
                    return
                if difference <= 4:
                    medal = "a Platinum medal."
                    gMedalsResults(medal,difference)
                    print("The number to guess was:", num)
                    return
            else:
                print("Your input was invalid please follow the rules.")
                guess = input("Please enter your guess as a number between 0 and 200: ")
        else:
            print("Your input was invalid please follow the rules.")
            guess = input("Please enter your guess as a number between 0 and 200: ")
                
def gMedalsResults(medal,difference):#Constructs printed results in guess medals
    print("You were off by,", difference, ",hence you have obtained", medal)
    
def main():
    choice = displayMenu()
    while choice != "3":
        if choice == "1":
            cornhole()
            print("\n")
            choice = displayMenu()
        elif choice == "2":
            guessMedals()
            print("\n")
            choice = displayMenu()

main()










