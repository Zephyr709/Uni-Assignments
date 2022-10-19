#SuperClass for heroes
class Hero():
    #Class variables
    __totalNumHeroes = 0
    __TotalNumChallengesMet = 0
    
    #Constructor
    def __init__(self, heroID = "N/A", lifeName = "N/A", altEgo = "N/A",
                 firstAppeared = 0, knownFor = "N/A", tool = "N/A", challengesMet = 0):
        
        self.__heroID = heroID
        self.__lifeName = lifeName
        self.__alterEgo = altEgo
        self.__firstAppeared = firstAppeared
        self.__knownFor = knownFor
        self.__toolOfStrength = tool
        self.__numOfChallengesMet = challengesMet
        
        Hero.__TotalNumChallengesMet += self.__numOfChallengesMet
        Hero.__totalNumHeroes += 1
        
    #Getters
    def getHeroID(self):
        return self.__heroID
        
    def getAlterEgo(self):
        return self.__alterEgo
        
    def getNumOfChallengesMet(self):
        return self.__numOfChallengesMet
    
    def getTotalChallenges():
        return Hero.__TotalNumChallengesMet
    
    #compares number of challenges met between two heroes
    #@param takes a second hero object to compare with
    #@return returns true if new hero is more experience
    #or returns false if old hero is more experienced
    def compareChallenges(self,obj2):
        if self.__numOfChallengesMet >= obj2.__numOfChallengesMet:
            return True
        if self.__numOfChallengesMet < obj2.__numOfChallengesMet:
            return False
    
    #Mutators
    
    #increases challenges met
    #@param takes an integer that represents the number of new challenges met
    def increaseChallengesMet(self, increase):
        self.__numOfChallengesMet += increase
        Hero.__TotalNumChallengesMet += increase
    
    #Special Methods
    #Overrides the print() and str() functions to return useful information
    def __str__(self):
        string = ("Superhero ID: " + self.__heroID + "\nReal life name: " + self.__lifeName +
                  "\nAlter ego: " + self.__alterEgo + "\nFirst appeared: " +
                  str(self.__firstAppeared) + "\nKnown for: " + self.__knownFor +
                  "\nTool of strength: " + self.__toolOfStrength + "\nNumber of challenges met: "
                  + str(self.__numOfChallengesMet) + "\n")
        return string

#Subclass
class MutatedHero(Hero):
    
    #Constructor
    def __init__(self,heroID = "N/A", lifeName = "N/A", altEgo = "N/A",
                 firstAppeared = 0, knownFor = "N/A", tool = "N/A", challengesMet = 0,
                 dayJob = "N\A", mutatedBy = "N/A"):
        
        super().__init__(heroID,lifeName,altEgo,firstAppeared,knownFor,tool,challengesMet)
        
        self.__dayJob = dayJob
        self.__mutatedBy = mutatedBy
        
    #Overrides the print/str function, returns the superclass override + subclass override 
    def __str__(self):
        superString = super().__str__()
        string = ("Day Job: " + self.__dayJob + "\nMutated By: " + self.__mutatedBy)
        return superString + string 
    
#Function to create and save hero list for ease of testing
#@param takes an empty list
#@returns a list of heroes entered by the user
def CreateHeroList(heroes):
    
    addHero = input("Would you like to enter a hero ? (Y/N) ").lower()
    
    while addHero == "y":
        mutated = input("is this hero mutated? (Y/N) ").lower()
        if mutated == "y":
            heroes.append(MutatedHero(input("Hero ID: "),input("Life Name: "),
                                      input("Alter Ego: "),int(input("First appeared: ")),
                                      input("Known For: "), input("Tool of Strength: "),
                                      int(input("Challenges Met: ")),input("Day Job: "),
                                      input("Mutated By: ")))
        elif mutated == "n":
            heroes.append(Hero(input("Hero ID: "),input("Life Name: "),
                               input("Alter Ego: "),int(input("First appeared: ")),
                               input("Known For: "), input("Tool of Strength: "),
                               int(input("Challenges Met: "))))
        
        addHero = input("Would you like to enter a hero ? (Y/N)").lower()

    return heroes

#main function
#@param Takes the list of heroes created for ease of testing
def main(heroes = []):
    if len(heroes) == 0:
        heroes.append(Hero("1234","Bruce Wayne", "Batman", 1939,
                           "Fighting Skills", "Bat-related Vehicle", 40))
        heroes.append(Hero("1543","Hal Jordan", "Green Lantern", 1940,
                           "Able to craft anything he can envision out of sheer willpower",
                           "Power Ring", 25))
        heroes.append(Hero("2234","T'Chala", "Black Panther", 1966,
                           "Enhanced Abilities", "Wakandan Tehcnology", 65))
        heroes.append(Hero("3334","Diana of Themyscira", "Wonder Woman", 1941,
                           "Superhuman Powers", "Lasso Of Truth", 30))
        heroes.append(MutatedHero("5545","Bruce Banner", "Hulk", 1962,
                           "Green Rage Machine","N/A", 45,"Scientist","Gamma Rays"))
        heroes.append(MutatedHero("4434","Steve Rogers", "Captain America", 1941,
                           "Enhanced to the peak of human perfection", "N/A",
                           56,"Artist","Super-Soldier Serum"))
        heroes.append(MutatedHero("6424","Peter Parker", "Spider-Man", 1962,
                           "Spider Related Abilities","N/A", 50,"Freelance Photographer",
                           "Radiactive Spider Bite"))
        heroes.append(MutatedHero("7777","Rex Mason", "Metamorpho", 1965,
                           "Can shapeshift into any element","N/A", 30,"Mercenary",
                           "Radioactivity of an ancient meteor"))
        
    print("Members of the Superheroes foundation\n\n")
    index = 0
    numChallenges = 0
    mostExpereincedHero = ""
    for i in range(len(heroes)):
        print(heroes[i], "\n", end ='\n')
        numChallenges += heroes[i].getNumOfChallengesMet()
        if i >= 1:
            if heroes[i].compareChallenges(heroes[index]):
                index = i
    mostExpereincedHero = heroes[index].getAlterEgo()  
    
    print("Superhero with most experience meeting challenges: ", mostExpereincedHero)
    print("Total number of heroes in the federation: ", len(heroes))
    if Hero.getTotalChallenges() == 0:
        print("Total number of challenges completed: ", numChallenges)
    else:
        print("Total number of challenges completed: ", Hero.getTotalChallenges())
    

#creates empty list and passes it to the create hero list function
newList = input("Would you like to create a new hero list? (Y/N) ").lower()
if newList == "y": 
    heroes = []
    CreateHeroList(heroes)
    main(heroes)
else:
    main()



    
    
    
    
    
    
    
        