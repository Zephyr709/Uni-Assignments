##
# This program is for a can producing company to keep track of orders
# and produce and store information on those orders
##

from math import pi, pow


class CanOrder():
    #Class Variables
    _NoOfOrders = 0
    _NextOrderNo = 100
    
    #Constructor
    def __init__(self, quantityOrdered = 0,radius = 0.0,
                 height = 0.0, handle = False):
        
        self._orderID = CanOrder._NextOrderNo
        self._quantityOrdered = quantityOrdered
        self._radius = radius
        self._height = height
        self._handle = handle
        
        CanOrder._NoOfOrders += 1
        CanOrder._NextOrderNo += 2
    
    #Special Method
    def __str__(self):
        
        string = ("Order ID: " + str(self._orderID) + ("\nCan Radius: %.2f" % self._radius) +
                  (" cm \nCan Height: %.2f" % self._height) + " cm \nQuantity Ordered: "
                  + str(self._quantityOrdered) + " cans \nHandle Needed? " + str(self._handle) +
                  ("\nTotal Surface Area: %.2f" % self.getTotalSurfaceArea()) +
                  (" sq. cm.\nTotal Cost: $%.2f" % self.getTotalCost())
                  )
        return string
        
        
        
    #Getters
    def getID(self):
        return self._orderID
    
    def getRadius(self):
        return self._radius
    
    def getHeight(self):
        return self._height
    
    def getTotalSurfaceArea(self):
        surfArea =(2*pi*pow(self._radius,2) + (2*pi*self._radius*self._height))
        return surfArea * self._quantityOrdered
    
    def getTotalCost(self):
        COST = 0.005
        COSTHANDLE = 0.50
        
        if self._handle:
            return (self.getTotalSurfaceArea()*COST) + (COSTHANDLE*self._quantityOrdered)
        else:
            return (self.getTotalSurfaceArea()*COST)
    
    def printNumOrders(self):
        print("The total number of orders received was " + str(CanOrder._NoOfOrders) + ".")
    
        
    #Setters
    def setRadius(self, radius):
        self._radius = radius
        print("The radius of cans for Order ID", self._orderID, "has been changed to",
              self._radius)
        print("The new cost for Order ID", self._orderID, "is $%.2f \n" % self.getTotalCost())
        
    def setHeight(self, height):
        self._height = height
        print("The height of cans for Order ID", self._orderID, "has been changed to",
              self._height)
        print("The new cost for Order ID", self._orderID, "is $%.2f \n" % self.getTotalCost())
    

        

def main():
    order1 = CanOrder(100,5,10)
    order2 = CanOrder(300,7.5,20,True)
    
    print(order1)
    print("")
    print(order2)
    print("")
    
    order2.setHeight(21)    
    
    order1.printNumOrders()
    
    print("The total cost of all orders received was $%.2f." % (order1.getTotalCost()+order2.getTotalCost()))

main()
    
    