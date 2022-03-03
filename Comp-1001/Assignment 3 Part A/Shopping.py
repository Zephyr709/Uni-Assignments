##
# This program constructs the users shopping list and returns
# a receipt containing the quantity of items, price and total cost
##

#Function definitions
def main():
    #list initializations
    produceList = ["Bin 1: Bag of Apples", "Bin 2: Banana Bunch",  
           "Bin 3: Pears", "Bin 4: Bag of Carrots", 
           "Bin 5: Cauliflower", "Bin 6: Broccoli", 
           "Bin 7: Red Bell Pepper", "Bin 8: Green Onions",  
           "Bin 9: Packaged Okra", "Bin 10: Oranges"]
    pricesList = [5.50, 2.60, 0.80, 3.25, 3.99, 3.35, 1.35, 1.10, 4.50, 0.80]
    shopList = [[]]
    itemsBought = 0
    
    #function Calls
    printOptions(produceList, pricesList)
    
    shopList, itemsBought = consShopList(pricesList)
    
    if itemsBought != 0: #only prints the receipt if user bought something
       printReceipt(shopList)

def printOptions(bins,prices): # this function prints the items and associated costs
    for i in range(len(bins)):
        print(bins[i], "{$" + str("%.2f" % prices[i]) + "}")
        

def consShopList(prices):
    shop = input("Do you wish to start filling your shopping cart? (yes/done) ").lower()
    shopList = [["Bin Num"], #initializes shopList with proper headers
                ["Quantity"],
                ["Total Cost"],
                ]
    itemsBought = 0
    
    while shop != "yes" and shop != "done": #prompts user again if format is incorrect
        shop = input("Please enter your choice in the proper format. (yes/done) ").lower()
    
    while shop == "yes":
        choice = input("Enter the bin number (e.g., enter 3 for Pears): ")
        quantity = input("Enter the quantity of the selected produce: ")
        while (not choice.isdigit()) or (not quantity.isdigit()) or (int(choice)>len(prices)) : #prompts user again if format is incorrect
            print("Please use the correct format for your answers.")
            
            choice = input("Enter the bin number (e.g., enter 3 for Pears): ")
            quantity = input("Enter the quantity of the selected produce: ")
        
        choice = int(choice)
        quantity = int(quantity)
        cost = quantity*prices[choice - 1]
        
        #appends bin number, quantity and cost to the shopping list
        shopList[0].append(choice)
        shopList[1].append(quantity)
        shopList[2].append(cost)
        
        itemsBought += 1
        
        shop = input("Do you wish to continue shopping? (yes/done) ").lower() #prompts user to keep shopping or quit
        
        while shop != "yes" and shop != "done": #prompts user again if format is incorrect
            shop = input("Please enter your choice in the proper format. (yes/done) ").lower()
        
        if shop == "done":
            print("Thanks for shopping, your receipt will be printed out momentarily.")
            return shopList, itemsBought
        
    if shop == "done": #prints a statement if the user buys nothing
        print("\nThanks for stopping by, buy some things next time! \n")
        return None, 0 #returns None to the shop list and 0 to items bought

        
        
        
def printReceipt(shopList):
    totalBill = 0
    for col in range(len(shopList[0])):
        
        for row in range(len(shopList)): #prints the elements of the list in a table and formats based on data type
            if col == 0:
                print("%-10s" % shopList[row][col], end = "")
            elif row == 0:
                print("%-10d" % shopList[row][col], end = "")
            elif row == 1:
                print("%-10d" % shopList[row][col], end = "")
            elif row == 2:
                print("%-10.2f" % shopList[row][col], end = "")   
        
        print("") #starts a new line after each row of the table is complete       
    
    for i in range(1,len(shopList[0])): #Adds up the cost of all items
        totalBill += shopList[2][i]
    
    print("\nThe total bill is $%.2f" % totalBill)
        

    
main()

