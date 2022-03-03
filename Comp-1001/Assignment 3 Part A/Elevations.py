##
# This program takes a list of elevations of town plots adn given a
# predicted elevation rise of the river returns a grid layout that shows
# the coordinates of unsubmerged sections of the town, and * for submerged
# sections of the town
##

def main():
    #initializes list and variable
    elevations = [[243, 479, 549, 470, 331, 20], 
                  [492, 454, 231, 366, 65, 32], 
                  [71, 534, 285, 345, 509, 5], 
                  [204, 249, 145, 54, 211, 46], 
                  [124, 217, 545, 160, 242, 203], 
                  [461, 236, 436, 391, 508, 68], 
                  [428, 176, 85, 435, 496, 191], 
                  [502, 238, 325, 144, 222, 95], 
                  [227, 504, 339, 132, 424, 298], 
                  [515, 202, 128, 54, 467, 307]]
    riverRise = input("Enter the expected river rise: ") 
    
    while not riverRise.isdigit():#validates user input and prompts if incorrect
        print("please enter the expected river rise as an integer.")
        riverRise = input("Enter the expected river rise: ")
    
    riverRise = int(riverRise) #converts user input to an integer
    
    #function calls
    elevations = convertElevations(elevations, riverRise)
    printList(elevations)
    
    
def convertElevations(elevations, riverRise): # this function converts the original list into coordinates or an asterix to indicate submerged
    for row in range(len(elevations)):
        for col in range(len(elevations[0])):
            if elevations[row][col] <= riverRise:
                elevations[row][col] = "*"
            else:
                elevations[row][col] = "%d,%d" % (row,col)
    
    return elevations
    
def printList(townPlot): # this function takes the modified list and converts it into a town plot
    for row in range(len(townPlot)):
        print("| ", end = "")
        for col in range(len(townPlot[0])):
            if townPlot[row][col] == "*" :
                print(" * ", end = "")
            else:
                print(townPlot[row][col], end = "")
            if (col + 1) != len(townPlot[0]):
                print(" | ", end = "")
        print(" |")

main()
    