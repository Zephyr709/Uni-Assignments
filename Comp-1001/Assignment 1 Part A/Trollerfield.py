##
# Assignment#1 Question 4
# This program calculates how much Trollers it would cost to construct a
# Trollerfield
##
from math import pi
# Constants
FT_PER_TRLLFT = 5
TRLLRS_PER_CAD = 50
FEE = 100           #CAD
COST_PER_FT = 20    #CAD

# Variables
length = (float(input("Enter length of the rectangle in trollfeet: ")))*FT_PER_TRLLFT
width = (float(input("Enter width of the rectangle in trollfeet: ")))*FT_PER_TRLLFT
majRadi = (float(input("Enter major radius of the ellipse in trollfeet: ")))*FT_PER_TRLLFT
minRadi = (float(input("Enter minor radius of the ellipse in trollfeet: ")))*FT_PER_TRLLFT

#Equations
ellipseArea = pi * majRadi * minRadi
rectArea = width * length 
totalArea = (ellipseArea*2) + rectArea
cadCost = (totalArea * COST_PER_FT) + FEE

trllrsCost = cadCost * TRLLRS_PER_CAD

print("The cost to construct a ",'%.2f' % totalArea , "sq ft field is ",'%.2f'% trllrsCost, "Trollars")

#print(ellipseArea, rectArea, totalArea, cadCost)




