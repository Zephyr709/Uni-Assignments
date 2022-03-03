##
# This program translates a given grade at the Geekland University
# into an eek grade.
##

#Functions

# This function converts the geek grade to an eek grade value
def ggConversion(grade):
    alpha = 111111
    beta = 11111
    gamma = 1111
    delta = 111
    epsilon = 11
    if (grade == "alpha"):
        grade = alpha
    elif (grade == "beta"):    
        grade = beta
    elif (grade == "gamma"):
        grade = gamma
    elif (grade == "delta"):
        grade = delta
    elif (grade == "epsilon"): 
        grade = epsilon
    
    return grade #returns the modified grade value

#Variables
geekName = input("Enter grade as Alpha, Beta, Gamma, Delta, or Epsilon: ")
gradeTag = input("Enter the Mu, Pu, or Nu: ")

#converts input strings to desired format
geekGrade = geekName.lower()
gradeTag = gradeTag.lower()
geekName = geekGrade.capitalize()

# Main block


# This block of code takes the geekGrade string value and converts it to an 
# eekValue to be used as needed

grade = geekGrade
    
alpha = 111111
beta = 11111
gamma = 1111
delta = 111
epsilon = 11
if (grade == "alpha"):
    grade = alpha
elif (grade == "beta"):    
    grade = beta
elif (grade == "gamma"):
    grade = gamma
elif (grade == "delta"):
    grade = delta
elif (grade == "epsilon"): 
    grade = epsilon

eekValue = grade



if (geekGrade == "alpha" or geekGrade == "beta" or geekGrade == "gamma"
    or geekGrade == "delta" ): #Checks the vailidity of user input in desired format
    
    #Makes changes to the eekValue based on the value of gradeTag
    if (gradeTag == "mu"):
        eekLength = len(str(eekValue))-1
        eekValue -= eekValue
        print("The Numeric eekValue of", geekName , "is:", str(eekValue) + ("0"*eekLength))
    
    elif (gradeTag == "pu"):
        eekValue += eekValue
        print("The Numeric eekValue of", geekName , "is:", eekValue)
    
    elif (gradeTag == "nu"):
        print("The Numeric eekValue of", geekName , "is:", eekValue)

#if geekGrade doesnt match other values, skips unnessecary steps        
elif (geekGrade == "epsilon"):  
    print("The Numeric eekValue of", geekName , "is:", eekValue)       
     
else:
    print("Please enter a valid grade and/or grade tag.")

 















