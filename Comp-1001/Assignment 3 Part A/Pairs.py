##
# This program takes a list of integers and determines which pairs add up to
# a particular given integer
##

def main():
    expectedSum = int(input("Enter the expected sum of two values: ")) #takes user input
    
    givenList = convertList()
    pairsList = []
    pairsList = findPairs(givenList, expectedSum)
    
    printResults(givenList, expectedSum, pairsList)
    
def convertList():# Converts user input into a list of integers
    userList = input("Enter the list of elements your working with seperated by ', ': ").split(", ") #turns user input into a list
    for i in range(len(userList)):#converts string list to integer
        userList[i] = int(userList[i])
    
    return userList
    
def findPairs(givenList, expectedSum): 
    # finds pairs of numbers from the given list (which are not the same) 
    # that add up to the the expected sum and returns them in a list
    
    k = 1      #intializes a variable k at 1 so the inner loop does not test element 0 against itself                     
    pairsList = [] #intializes an empty list for holding the list of pairs
   
    for i in range(len(givenList)): # Changes the index of element 1
        
        if k < len(givenList): # verifies that k is not outside the range
            
            for j in range(k,len(givenList)): #Changes the index of element 2 
            
                if givenList[i] != givenList[j]: #verifies that element 1 and element 2 are not the same
                    element1 = givenList[i] #intializes variables with element 1 and 2 to test
                    element2 = givenList[j]
                    
                    if (element1+element2) == expectedSum: # checks to see if element 1 and 2 meet the requirements for a pair
                        pairsList.append([element1,element2]) #appends the elements to list
        
        k += 1 #increments k so there are no calculations with two of the same elements
    
    return pairsList #returns the list of pairs
        
def printResults(givenList, expectedSum, pairsList):
    print("The given list is:", givenList)
    print("The list of pairs that add to the given sum of", expectedSum , 
          "is:")
    for i in range(len(pairsList)):
        print("(", end="")
        for j in range(len(pairsList[i])):
            print(pairsList[i][j], end = "")
            if j + 1 != len(pairsList[i]):
                print(",", end = "")
        print(")")



main()

