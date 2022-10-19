##
# This program calculates and produces information relevant to the 
# Sphere Alliance
##

class SphereAlly():
    #Class Variables
    _TotalAlliancePop = 0
    _TotalFOLContribution = 1000
    
    #Constructor
    def __init__(self, sphereName = "Unknown", repName = "Unknown", population = 0,
                 fruitsOfLabour = 0.0, contribPer = 0.0):
        """ SphereName = name of sphere ally, repName = name of representative,
        Population = population of sphere ally, fruitsOfLabour = general funds on hand 
        that the ally is able to maintain regularly, contribPer = percentage of FOL willing
        to contribute to the alliance """
        
        self._sphereName = sphereName
        self._repName = repName
        self._population = population
        self._FOL = fruitsOfLabour
        self._contribPer = contribPer
        self._contribution = 0
        
        
        self._perCapitaFOL = self.computePerCapita()
        self._contribution += self.addContribution()
        SphereAlly._TotalFOLContribution += self.addContribution()
        SphereAlly._TotalAlliancePop += self._population
        
    #Getters
    def getSphereName(self): # Gets sphere name
        return self._sphereName
    
    def getRepName(self): # Gets representative name
        return self._repName
    
    def getPopulation(self): # gets population
        return self._population
    
    def printAllianceInfo(self):
        print("Total Population for all Sphere Allies: %d \nTotal FOL contributions from all Sphere Allies: %.2f sphere coin(s) \n" 
              % (SphereAlly._TotalAlliancePop, SphereAlly._TotalFOLContribution))
        
    #Setters
    #Updates ally population and aliance population
    #@param takes a number that represents a percentage change in pop
    def updatePopulation(self,percentChange): 
        SphereAlly._TotalAlliancePop += (int(self._population * percentChange) - self._population )
        self._population = int(self._population * percentChange)
        
        
        #Prints useful information relative to the changes made by the method
        print("The updated population for", self._sphereName, "is", self._population)
        print("The updated per capita FOL is %.2f \n" % self.computePerCapita(), end = "\n")
        
    #Method to return the Fruits of labor contribution for a sphere ally
    def addContribution(self):
        return self._FOL * self._contribPer
    
    #Method to computer average individual fruits of labor contribution
    def computePerCapita(self):
        return self._FOL / self._population
    
    #Method to compare per capita FOL
    #@param a second object of type SphereAlly
    def compareAllyPerCapFOL(self, obj2):
        if self._perCapitaFOL > obj2._perCapitaFOL:
            print(self._sphereName, "has higher per capita FOL funds.")
        if self._perCapitaFOL < obj2._perCapitaFOL:
            print(obj2._sphereName, "has higher per capita FOL funds.")
    
    #Special Methods
    def __str__(self):#Overrides the print function
        string = ("\nSphere Name: %s \nRep Name: %s \nPopulation: %d \nContributions: %.2f sphere coin(s) \nPer Capita FOL Funds: %.2f " % (self._sphereName, self._repName,
                  self._population, self._contribution, self.computePerCapita()))
    
        return string
    
def main():
    
    ally1 = SphereAlly("Sphereogamma","Emma Gamma", 5100,10000,0.02)
    ally2 = SphereAlly("Sphereodelta", "Pelta Delta", 8100,20500,0.03)
    
    print(ally1,"\n" , ally2, "\n")
    
    ally1.updatePopulation(0.9)
    ally2.printAllianceInfo()
    
    ally1.compareAllyPerCapFOL(ally2)
    
main()
    
        
        
        
        
        