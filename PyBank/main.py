#import library
import os
import csv
from pathlib import Path

# path to collect data from the Resources folder
budget_data = os.path.join("Resources", 'budget_data.csv')

# open the budget data file as a csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # initialize variables to store information
    profit = []
    months = []

    #read through each row of data following header
    for rows in csvreader:
        
        # append totals for profit and months
        profit.append(int(rows[1]))
        months.append(rows[0])

    # initialize variable for average change 
    average_change = []

    for x in range(1, len(profit)):
        average_change.append((int(profit[x]) - int(profit[x-1])))
    
    # determine average change in "Profit/Losses" between months over the entire period
    revenue_change = (round(sum(average_change) / len(average_change),2))
 
    # determine total months
    total_months = len(months)

    # determine greatest increase in profits over the entire period
    greatest_increase = max(average_change)
    
    # determine greatest decrease in losses over the entire period
    greatest_decrease = min(average_change)

# print the analysis
print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(sum(profit)))
print("Average Change: " + "$" + str(revenue_change))  
print("Greatest Increase in Profits: " + str(months[average_change.index(max(average_change))+1]) + " " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(months[average_change.index(min(average_change))+1]) + " " + "$" + str(greatest_decrease))

# export the results
file = open("pybank_results.txt","w")
    
# output the text file
file.write("Financial Analysis")
file.write("\n")
file.write("----------------------------")
file.write("\n")
file.write(f"Total Months: " + str(total_months))
file.write("\n")
file.write(f"Total: " + "$" + str(sum(profit)))
file.write("\n")
file.write(f"Average Change: " + "$" + str(revenue_change))
file.write("\n")
file.write(f"Greatest Increase in Profits: " + str(months[average_change.index(max(average_change))+1]) + " " + "$" + str(greatest_increase))
file.write("\n")
file.write(f"Greatest Decrease in Profits: " + str(months[average_change.index(min(average_change))+1]) + " " + "$" + str(greatest_decrease))
file.close()