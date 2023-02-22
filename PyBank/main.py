"""
# loop through the csv file to find: 
    
    -The total number of months included in the dataset

    -The net total amount of "Profit/Losses" over the entire period

    -The changes in "Profit/Losses" over the entire period, and then the average of those changes

    -The greatest increase in profits (date and amount) over the entire period

    -The greatest decrease in profits (date and amount) over the entire period
"""

import os
import csv

# direct to the csv file we need to open and read 
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")
    # print(budget_data_csv_path)
    # print(os.getcwd())
os.chdir(os.path.dirname(os.path.realpath(__file__)))
    # print(os.getcwd())

# file to hold the financial analyis summary 
outputFile = os.path.join("analysis", "financialAnalysis.txt")

with open(budget_data_csv_path, "r") as csvFile:
    csvRead = csv.reader(csvFile, delimiter=",")

    next(csvRead)

    # Delcare variables 
    count_months = 0
    total_revenue = 0
    monthly_change = 0
    previous_month = 0
    monthly_changes = []
    max_change = 0
    min_change = 0
    max_date = ""
    min_date = ""

    for row in csvRead:
        count_months += 1
     # print(count_months)
        pl = int(row[1])
        total_revenue += pl 
        if count_months > 1:
            monthly_change = pl - previous_month
            monthly_changes.append(monthly_change)
        if monthly_change > max_change:
            max_change = monthly_change
            pl_date=row[0]
            max_date = pl_date
        if monthly_change < min_change: 
            min_change = monthly_change
            pl_date=row[0]
            min_date = pl_date

        previous_month = pl   # set up for next row

avg_profit_loss = sum(monthly_changes) / len(monthly_changes)
avg_profit_loss = round(avg_profit_loss, 2)

# print(avg_profit_loss)
# print(max_date)

# Print statements

all_outputs = (

f"\nFinancial Analysis \n"

f"\n----------------------- \n"

f"\nTotal Months: {count_months} \n"

f"\nTotal: ${total_revenue} \n"

f"\nAverage Change: ${avg_profit_loss} \n"

f"\nGreatest increase in Profits: {max_date}, ${max_change} \n"

f"\nGreatest increase in Profits: {min_date}, ${min_change} \n"
)


# Export all outputs to the financialAnalyis.txt file
with open(outputFile, "w") as textFile:
    textFile.write(all_outputs)


    print(all_outputs)
    




