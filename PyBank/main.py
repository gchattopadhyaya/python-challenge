# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

TotalMonth = 0
TotalProfitLosses = 0
TotalAverageChange = 0
AverageChange = 0
minpos = 0
maxpos = 0
Date = []
Profit_Losses = []
AverageChangeList = []
AverageChangeDate = []

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        Date.append(row[0])
        Profit_Losses.append(row[1])
        TotalMonth = TotalMonth+1
     
    #Remove the first element of Date List
    Date.pop(0)
    print (f"Total Month Count: {len(Date)}")
    
    #Remove the first element of the Profit and Losses list
    Profit_Losses.pop(0)
    for element in Profit_Losses:
            TotalProfitLosses+=int(element)
    
    print(f"Total Profit And Losses Count: {TotalProfitLosses}")

    for i in range(len(Profit_Losses)-1):
        AverageChangeList.append(int(Profit_Losses[i+1]) - int(Profit_Losses[i]))
        AverageChangeDate.append(Date[i+1])
        
    for element in AverageChangeList:
        TotalAverageChange+=int(element)
        
    AverageChange = TotalAverageChange/len(AverageChangeList)
    
    print(f"Average Change: {AverageChange}")
    
    maxpos = AverageChangeList.index(max(AverageChangeList)) 
    print(f"Greatest Increase in Profits:{AverageChangeDate[maxpos]} {max(AverageChangeList)}")
    
    
    minpos = AverageChangeList.index(min(AverageChangeList))  
    print(f"Greatest Decrease in Profits:{AverageChangeDate[minpos]} {min(AverageChangeList)}")
     
    # Specify the file to write to
    output_path = os.path.join("..", "output", "OutputOfPyBank.csv")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Total Month Count:', len(Date)])

        # Write the second row
        csvwriter.writerow(['Total Profit And Losses Count:', TotalProfitLosses])
    
        # Write the third row
        csvwriter.writerow(['Average Change:', AverageChange])
    
        # Write the fourth row
        csvwriter.writerow(['Greatest Increase in Profits:', AverageChangeDate[maxpos], max(AverageChangeList)])
    
        # Write the fifth row
        csvwriter.writerow(['Greatest Decrease in Profits:', AverageChangeDate[minpos], min(AverageChangeList)])
    
    