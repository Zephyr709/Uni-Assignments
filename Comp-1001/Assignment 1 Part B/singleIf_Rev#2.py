##
# This program prints out if the box is pretty heavy or not pretty
# heavy with only one if statement
##

boxWeight = float(input("Please enter the weight of the box: "))

boxOutput = "pretty heavy"

if boxWeight < 70:
    boxOutput = "pretty not to heavy"

print("The box is", boxOutput)
