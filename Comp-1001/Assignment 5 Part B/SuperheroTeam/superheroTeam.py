

#START OF GIVEN CODE
class Superhero:
    def __init__(self, hid="N/A", altEgo="N/A", \
                known="N/A", challenges=0):
        self.__heroID = hid
        self.__alterEgo = altEgo
        self.__knownFor = known
        self.__numOfChallengesMet = challenges

    def getID(self):
        return self.__heroID

    def getAlterEgo(self):
        return self.__alterEgo

    def getKnownFor(self):
        return self.__knownFor

    def getNumOfChallengesMet(self):
        return self.__numOfChallengesMet

    def __str__(self):
        return("%-10s %-15s %-20s %-4d" % \
                (self.__heroID, self.__alterEgo, \
                self.__knownFor, self.__numOfChallengesMet))
#END OF GIVEN CODE

def readHeroFile(heroFileName = ""):#opens a file given the name by the user and creates a list of superhero objects
    heroList = []
    hero = []
    while True:
        try:
            if heroFileName == "":
                heroFileName = input("Enter the name of the hero file: ")
            heroFile = open(heroFileName, "r")
        
        except FileNotFoundError as exception:
            print(exception)
        except Exception as exception:
            print(exception)
        
        else:
            line = heroFile.readline()
            
            while line != "":
                hero = line.split(",") #splits the line and stores hero info in a list
                heroList.append(Superhero(hero[0],hero[1],hero[2],int(hero[3])))#Passes the elements of the list as parameters for the object
                line = heroFile.readline()
                
            return heroList

def createTeams(heroList,heroTeam1,heroTeam2,notSelected):#Iterates through the Hero list and appends the heroes to the appropriate lists then returns the constructed lists

    for i in range(len(heroList)):
        if heroList[i].getKnownFor().lower() == "strength" or heroList[i].getKnownFor().lower() == "speed" or heroList[i].getKnownFor().lower() == "telekinesis":
            heroTeam1.append(heroList[i])
        elif heroList[i].getKnownFor().lower() == "intelligence" or heroList[i].getKnownFor().lower() == "invincibility" or heroList[i].getKnownFor().lower() == "telepathy":
            heroTeam2.append(heroList[i])
        else:
            notSelected.append(heroList[i].getAlterEgo())
    
    return heroTeam1,heroTeam2,notSelected

def printTeams(heroTeam1,heroTeam2):
    #Prints hero team 1 in the desired format
    print("Members of Team 1 to face Thanos")
    print("%-10s %-15s %-20s %-4s" % ("Hero ID","Alter Ego", "Known For","Challenges Met"))
    for element in heroTeam1:
        print(element)
    
    #Prints hero team 2 in the desired format
    print("\nMembers of Team 2 to face Hela")
    print("%-10s %-15s %-20s %-4s" % ("Hero ID","Alter Ego", "Known For","Challenges Met"))
    for element in heroTeam2:
        print(element)

def saveNotSelected(notSelected,writeFileName = ""):
    while True:
        try:
            if writeFileName == "":
                writeFileName = input("Enter the name of the file you wish to write to: ")
            writeFile = open(writeFileName,"w")
        except FileNotFoundError as exception:
            print(exception)
        except Exception as exception:
            print(exception)
        else:
            for element in notSelected:
                writeFile.write(element + "\n")
            break
        finally:
            writeFile.close()

def main():
    #prompts for use of default file names and intializes them if yes
    default = input("Would you like to use the default file names? (Y/N) ").lower()
    heroFileName = ""
    writeFileName = ""
    if default == "y":
        heroFileName = "heroes.txt"
        writeFileName = "not_selected.txt"

    #fills the hero list from the file
    heroList = readHeroFile(heroFileName)

    #intializes lists
    heroTeam1 = []
    heroTeam2 = []
    notSelected = []

    #calls the create teams function and populates the respective lists
    heroTeam1,heroTeam2,notSelected = createTeams(heroList,heroTeam1,heroTeam2,notSelected)

    #Prints out the teams
    printTeams(heroTeam1,heroTeam2)
    #writes the not selected heros to a file and saves it
    saveNotSelected(notSelected,writeFileName)

main()