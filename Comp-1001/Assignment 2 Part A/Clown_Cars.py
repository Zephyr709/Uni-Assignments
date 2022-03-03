##
# This program determines by rating of the council members what use if any
# the newly selected clowncars will have in clownville
##

# Libraries
from random import randint

# Variable Initialization
emergUse = "will be purchased for emergency use."
transpo = "will be leased for non-clown transportation."
intro = "Vehicle with plate number"
cont = "YES"

numCnclMems = 15
carsPurchased = 0

#Main block

while (cont == "YES"):  #Verifies that user wishes to process another car
    councilRatings = "" #Resets council ratings list for the next loop
    total = 0           #Resets total sum of ratings for the next loop
    avgRating = 0       #Resets the avg rating value for the next loop
    
    plateNum = input("Enter the license plate number: ") # Obtains plate number

    for i in range(numCnclMems):
        rating = randint(1,5) # Generates a rating of 1-5
        total = total + rating # Contains the total sum of ratings
        councilRatings = councilRatings + str(rating) + " " # Concatenates the ratings
    
    avgRating = total/numCnclMems
        
    if avgRating >= 3:
        print("Council Member's ratings:", councilRatings)
        print("Average Rating: ","%.2f" %avgRating)
        print(intro, plateNum, emergUse)
        carsPurchased += 1

    elif avgRating >= 2:
        print("Council Member's ratings:", councilRatings)
        print("Average Rating:", "%.2f" %avgRating)
        print(intro, plateNum, transpo)
 
    else:
        print("Council Member's ratings:", councilRatings)
        print("Average Rating:", "%.2f" %avgRating)
        print(intro, plateNum, "will not be used.")
    
    # Takes the user input and converts it to the correct capitalization
    process = input("Do you want to process another clown car? (YES or NO) ")
    cont = process.upper()
    
    while (cont != "YES") and (cont != "NO"): # Validates user input
        print("Please enter your answer in the proper format.")
        process = input("Do you want to process another clown car? (YES or NO) ")
        cont = process.upper()
        
        
print("The total number of cars purchased for the Clown Emergency Fleet is",
      carsPurchased)
    
    


