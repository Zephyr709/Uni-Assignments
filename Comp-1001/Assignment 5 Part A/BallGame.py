#This program simulates a ball game in the kingdom of trolls

from random import randint

#recursive function that keeps playing the game until the golden ball is found
def burstingBalls(randomInt):
    goldenBall = randint(1,10) #generates value for base case
    if goldenBall > 7: #Base case
        print("Burst! %d balls created per ball. Golden ball located." % randomInt)
        return randomInt
    else:#recursive call
        print('Burst! %d balls created per ball.' % randomInt)
        return randomInt * burstingBalls(randomInt)
    
#Main function    
def main():
    num = randint(2,6)
    
    player1 = input("Enter the first player's name: ")
    player1Balls = burstingBalls(num) #Stores player 1s game 
    
    player2 = input("Enter the second player's name: ")
    player2Balls = burstingBalls(num)#stores player 2s game
    
    #Prints game info
    print("Balls generated on last burst for %s is: %d" % (player1, player1Balls))
    print("Balls generated on last burst for %s is: %d" % (player2, player2Balls))
    
    if player1Balls < player2Balls:
        print("Winner:", player1)
    elif player1Balls > player2Balls:
        print("Winner:", player2)
    else:
        print("The game was a tie.")
        
        
main()