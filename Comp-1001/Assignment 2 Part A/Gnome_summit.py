##
# This program calculates how many times it takes for a gnome to climb
# a mountain given height of the mountain and drop-off point in metres
##

# imported libraries and functions
from random import randint

#Variables
#Takes the needed input from the user
height = int(input("Enter the height of the mountain: "))
dropPoint = int(input("Enter the height of the cable car drop point: "))

#intializes needed variables
heightToClimb = height - dropPoint
heightClimbed = 0
napNum = 0

#Main
while heightClimbed < heightToClimb:
    heightClimbed += 30 #adds 30m to height traveled after every nap
    iceNap = randint(0,1) #randomly generates conditons for an icy nap or not
        
    #adds to the nap number if gnome is not at the top
    if heightClimbed < heightToClimb:
       napNum += 1
    
    
    if iceNap == 1: #if gnome slid during his nap deducts 8m off height
        heightClimbed -= 8
        print("Uh oh!  Zeph slid during nap number", str(napNum) + "!")

print("It took Zeph", napNum, "tries to climb", heightToClimb, "metres \n" + 
      "from the cable car drop off point to the summit.")



