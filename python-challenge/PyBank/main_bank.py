#!/usr/bin/env python
# coding: utf-8
import os
import csv

budget_path = os.path.join("budget_data2.csv")

with open(budget_path, newline='') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=',')
    dates = []
    profits = []
    changes = []
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        dates.append(row[0])
        profits.append(int(row[1]))

    for row in range(1, len(profits)):
        changes.append(profits[row] - profits[row-1])
        averagechange = round(sum(changes)/len(changes),2)
        maxchange = max(changes)
        minchange = min(changes)
        maxchangedate = str(dates[changes.index(max(changes))])
        minchangedate = str(dates[changes.index(min(changes))])
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(dates)}")
    print(f"Total: ${sum(profits)}")
    print(f"Average Change: ${averagechange}")
    print(f"Greatest Increase in Profits: {maxchangedate} (${maxchange})")
    print(f"Greatest Decrease in Profits: {minchangedate} (${minchange})")

output_path = os.path.join("pyBanktxt.txt")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {len(dates)}"])
    csvwriter.writerow([f"Total: ${sum(profits)}"])
    csvwriter.writerow([f"Average Change: ${averagechange}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {maxchangedate} (${maxchange})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {minchangedate} (${minchange})"])

# In[ ]:




