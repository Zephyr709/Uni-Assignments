##
# This program decodes Yetian into english 
##

#Functions
def isValidYeti(yetiMsg): # checks the validity of the Yeti message format
    if yetiMsg.isdigit():
        return (len(yetiMsg)%3) == 0
    
    else:
        return False
    
def decodeDigits(digits): #converts string of digits to integers, gets asci Char
    if digits == "089": #checks if set of digits represents a " " in the yetian decoder
        return " "
    else:
        return chr(int(digits)) #returns asci Char

def decodeMsg(yetiMsg): # decodes the yeti message into english
    if isValidYeti(yetiMsg):
        j = 3
        string = ""
        for i in range(0,len(yetiMsg), 3): # loop goes through the yeti message in chunks of 3
           string = string + decodeDigits(yetiMsg[i:j]) #extracts 3 digit asci codes
           j += 3
        print("Yeti Message:", yetiMsg)
        print("English Translation:", string)
        
    else:
        print("The string is not a valid Yeti message.")
    

def main(): # takes user input and calls functions to decode the yeti message
    yetiMsg = input("Enter the Yeti message: ") 
    decodeMsg(yetiMsg)


main()    






