#This program deals with the backend of a bead shop, reading files containing info relevant to the shop and writing results to a seperate file

from tkinter import Y


def readPricelist(lst,stockFileName = ""):#reads the price list file, formats and stores the information in a list
    while True:
        try:
            if stockFileName == "":
                stockFileName = input("Enter the name of the stock file: ")
            stockFile = open(stockFileName,"r")
        #Exception Handling
        except FileNotFoundError as exception:
            print(exception)
        except Exception as exception:
            print(exception)
        else:
            
            line = stockFile.readline()
            i = 0
            while line != "":
                lst.append(line.split(","))
                lst[i][1] = int(lst[i][1])
                lst[i][2] = float(lst[i][2])  
                i += 1
                line = stockFile.readline()
            return lst
            

def readOrder(orderList,orderFileName = ""):#reads the order list file, formats and stores the information in a list
     while True:
        try:
            if orderFileName == "":
                orderFileName = input("Enter the name of the order file: ")
            orderFile = open(orderFileName,"r")
        #Exception Handling
        except FileNotFoundError as exception:
            print(exception)
        except Exception as exception:
            print(exception)
        else:
            line = orderFile.readline()
            i = 0
            while line != "":
                orderList.append(line.split(","))
                orderList[i][1] = int(orderList[i][1])
                i += 1
                line = orderFile.readline()

        return orderList


def writeResults(lst,resultFileName = ""):#writes the results of the program to a file
     while True:
        try:
            if resultFileName == "": 
                resultFileName = input("Enter the name of the file to save results: ")
            resultFile = open(resultFileName,"w")
        #Exception Handling
        except FileNotFoundError as exception:
            print(exception)
        except Exception as exception:
            print(exception)
        
        else:
            string = ""
            for row in range(len(lst)):
                string = ""
                for col in range(len(lst[0])):
                    string += str(lst[row][col])
                    if col < (len(lst[0]) -1):
                        string += ","
                
                if lst[row][1] < 5:
                    string += " ORDER MORE"

                string += "\n"
                resultFile.write(string)
            break
        finally:
            resultFile.close()

def printSummary(orderList): #prints the summary of the orders in desired format
    print("%-11s %-15s %-15s" %("Bead Code", "Quant Ordered", "Total Price"))
    totalRev = 0
    try:
        for row in range(len(orderList)):
            for col in range(len(orderList[0])):
                if col == 0:
                    print("%-11s" % orderList[row][col], end = "")
                elif col == 1:
                    print("%-15d" % orderList[row][col], end = "")
                elif col == 2:
                    print("$%-15.2f" % orderList[row][col], end = "")
                    totalRev += orderList[row][col]
            print()
        print("Total Revenue: $%.2f" % totalRev )
    #Exception Handling
    except IndexError:
        print("Please run the update stock and summary function before attempting to print the summary")
    except Exception as exception:
        print(exception)

def updateStockAndSummary(beadList, orderList):#Updates the stock of the bead list and appends the total price of an order to order list
    
    for i in range(len(orderList)):
        index = 0
        #Searches the bead list to match the bead of the order list
        for j in range(len(beadList)):
            if beadList[j][0] == orderList[i][0]:
                index = j
                break

        beadList[index][1] -= orderList[i][1] 
        orderList[i].append(beadList[index][2]*orderList[i][1])

    return beadList, orderList

def main():
    #Optional initiation of file names
    defaultNames = input("Would you like to use the default file names? (y/n)").lower()
    if defaultNames == "y":
        stockFileName = "bead_pricelist.txt"
        orderFileName = "bead_order.txt"
        resultFileName = "result_bead_list.txt"
    else:
        stockFileName = ""
        orderFileName = ""
        resultFileName = ""

    #intializing empty lists
    beadList = [] 
    orderList = [] 
    
    #Function calls to read files
    beadList = readPricelist(beadList,stockFileName)
    orderList = readOrder(orderList,orderFileName)

    #function calls to update lists, print summary, and write results
    beadList,orderList = updateStockAndSummary(beadList,orderList)
    printSummary(orderList)
    writeResults(beadList,resultFileName)


main()
