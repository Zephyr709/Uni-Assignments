##
# This program computes how much time a worker bee has worked 
# in bee time
##

#libraries
from math import pow

#Constants
X = 30
BROKS_PER_BRIK = pow(X,1)
BRINS_PER_BRIK = pow(X,2)
BRONS_PER_BRIK = pow(X,3)

#Variables
briks = float(input("Enter number of briks worked, a value between 0 and 99999: "))

#Main Block
if (briks >= 0) and (briks <= 99999):
    brons = briks//BRONS_PER_BRIK
    briks = briks%BRONS_PER_BRIK 
    #print("Briks: ", briks)
    
    brins = briks//BRINS_PER_BRIK
    briks = briks%BRINS_PER_BRIK
    #print("Briks: ", briks)
    
    broks = briks//BROKS_PER_BRIK
    briks = briks%BROKS_PER_BRIK
    #print("Briks: ", briks)
    
    if (briks < 10):
       briks = '0' + str(int(briks))  
    else:
       briks = str(int(briks))
       
    if (broks < 10):
        broks = '0' + str(int(broks))    
    else:
        broks = str(int(broks))
    
    if (brins < 10):    
        brins = '0' + str(int(brins))    
    else:
        brins = str(int(brins))    
   
    if (brons < 10):    
        brons = '0' + str(int(brons))    
    else:
        brons = str(int(brons))    
    
    print("Time worked (brons:brins:broks:briks) is " + brons + ':' + brins +
          ':' + broks + ':' + briks)
else:
    print("Please enter a valid amount of bee time between 0 and 99999.")