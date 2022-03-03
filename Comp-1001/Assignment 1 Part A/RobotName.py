##
# Creates a model number for a robot based on the information 
# of the engineer who designed it
##

#Needed Libraries 
import math

#Variables
engName = input("Enter the engineer's nickname: ")
engAge = int(input("Enter the engineer's age: "))
engServ = float(input("Enter the engineer's years of service: "))

# Equations

letter1 = engName.lower()[0]
letter2 = engName.upper()[len(engName)-1]

rbtNum = str(math.trunc(( engAge + engServ )*5))
modlStart = (letter1 + letter2 + "#")
modlNum = modlStart + (rbtNum + rbtNum[::-1]) * 2

print("the robot " + engName + " has model number " + modlNum)

# Test code to verify proper values are being stored throughout the program
print(letter1, letter2, "\n")
print(rbtNum, "\n")
print(modlStart)
print("\n" + modlNum, "\n")
