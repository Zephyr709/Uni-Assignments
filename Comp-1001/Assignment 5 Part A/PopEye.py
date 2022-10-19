#Recursive program to fine out how many boxes Popeye needs to open 
#to get his spinach

#Counts how many boxes popeye needs to open to find the spinach
def CountBoxes(tinList):
    if tinList[0] == "spinach":#Base Case
        return 1
    else: 
        tinList.pop(0) #Simplifies the problem
        return 1 + CountBoxes(tinList)

def main():
    tinLabels = ["mushroom soup", "creamed corn", \
                 "apple pie filling", "kidney beans", \
                     "chili", "custard", "peas and carrots", \
                         "spaghetti sauce", "sprouts", \
                             "green beans", "spinach", \
                                 "tuna", " tomato paste "]
    
    numOpened = CountBoxes(tinLabels)
    print("Number of boxes that Popeye opens before getting spinach:", numOpened)

main()