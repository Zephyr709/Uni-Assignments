#Super class
class TaxiFare():
    _TotalFaresCollected = 0.0
    
    #Constructor
    def __init__(self, taxiID = "000", operator = "unknown"):
        self._taxiID = taxiID
        self._operator = operator
        self._charges = 0
        
        
        
    #Getters
    def getTaxiID(self):
        return self._taxiID
    
    def getOperator(self):
        return self._operator
    
    def getTotalFares(self):
        return TaxiFare._TotalFaresCollected
    
    #Setters
    def computeCharges(self):
        self._charges = 0
        
        return 0
    
    #Special Methods
    #Overrides the print() and str() functions to return useful information
    def __str__(self):
        string = ("Taxi ID: " + self._taxiID + "\nOperator: " + self._operator +
                  "\nCharges: $%.2f \n" % self._charges)
        return string
    
class CabFare(TaxiFare):
    _costPerKM = 1.75
    _costPerMin = 0.50
    
    #Constructor
    def __init__(self,taxiID = "000", operator = "unknown",
                 meteredKMs = 0.0, waitTime = 0):
        
        super().__init__(taxiID,operator)
        self._meteredKMs = meteredKMs
        self._waitTime = waitTime
        
    #Getters
    def getMeteredKMs(self):
        return self._meteredKMs
    
    def getWaitTime(self):
        return self._waitTime
    
    #Setters
    def computeCharges(self):
        self._charges = (CabFare._costPerKM * self._meteredKMs +
                CabFare._costPerMin * self._waitTime)
        return self._charges
    
    #Special methods
    #Overrides the print() and str() functions to return useful information
    def __str__(self):
        superString = super().__str__()
        string = ("Number of KMs: %.2f \nWait time: %d Minutes \n" % (self._meteredKMs,self._waitTime))
        return superString + string
    
class WaterTaxiFare(TaxiFare):
    
    #Constructor
    def __init__(self,taxiID = "000", operator = "unknown",
                 numTickets = 0, costPerTicket = 0.0):
        
        super().__init__(taxiID,operator)
        self._numTickets = numTickets
        self._costPerTicket = costPerTicket
        
    #Getters
    def getNumTickets(self):
        return self._numTickets
    
    def getCostPerTicket(self):
        return self._costPerTicket
    
    #Setters
    def computeCharges(self):
        self._charges = (self._numTickets*self._costPerTicket)
        return self._charges
    
    #Special methods
    #Overrides the print() and str() functions to return useful information
    def __str__(self):
        superString = super().__str__()
        string = ("Number of tickets: %d \nCost per ticket: $%.2f \n" % (self._numTickets,self._costPerTicket ))
        return superString + string
    
class CharterWaterFare(WaterTaxiFare):
    #Constants related to the class
    _costToD1 = 25.50
    _costToD2 = 33.75
    _costToD3 = 48.0
    
    #Constructor
    def __init__(self,taxiID = "000", operator = "unknown",
                 numTickets = 0, costPerTicket = 0.0,
                 destination = "N/A"):
        
        super().__init__(taxiID,operator,numTickets,costPerTicket)
        self._destination = destination
    
    #Getters
    def getDestination(self):
        return self._destination
    
    #Setters
    def computeCharges(self):
        superCost = super().computeCharges()
        if self._destination == "D1":
            self._charges = superCost + self._costToD1
            return self._charges
        if self._destination == "D2":
            self._charges = superCost + self._costToD2
            return self._charges
        if self._destination == "D3":
            self._charges = superCost + self._costToD3
            return self._charges
        else:
            self._charges = 0
            return self._charges
        
    #Special methods
    #Overrides the print() and str() functions to return useful information
    def __str__(self):
        superString = super().__str__()
        string = ("Destination: " + self._destination + "\n")
        return superString + string
        
    
def main():
    fares = []
    fares.append(TaxiFare("222","Leah"))
    fares.append(CabFare("333","Rae",20.5,10))
    fares.append(WaterTaxiFare("444","Skipper",15,3.50))
    fares.append(CharterWaterFare("555","Nate",10,2.50,"D3"))
    fares.append(CharterWaterFare("777","Bob",5,1.50,"D5"))
    
    totalFares = 0
    
    for i in range(len(fares)):
        totalFares += fares[i].computeCharges()
        print(fares[i])
    
    print("Total Fares Collected: $%.2f " % totalFares)

main()
    
    
    
    
                






        
        