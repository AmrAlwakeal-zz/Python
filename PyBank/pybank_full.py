import csv 
import os 
budget_csv = os.path.join('python_challenge/PyBank/Resources/budget_data.csv')

# variables 
months = 0 
profit = []
month = []
change_month = []
# open file and iteration 
with open (budget_csv, 'r') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')
    csv_header= next(csv_read)
    for row in csv_read:
        month.append(str(row[0]))
        total_months = len(month)
        profit.append(float(row[1]))
        total_profit = sum(profit)
        highest_increase = max(profit)
        lowest_decrease = min(profit)
        min_index = profit.index(lowest_decrease)
        min_month = month[min_index]
        max_index = profit.index(highest_increase)
        max_month = month[max_index]
        month_start = month[0]
        month_end = month[-1]
        # average change/ year
        change_month = [(float(profit[i+1]- profit[i]) / profit[i]) for i in range(len(profit)-1)]
        total_change = sum(change_month) / 12
        average_change = total_change * 100

# average change/month = 2nd month - 1st month / 1st month  
# define 1st month then iterate the rest
# sum average change/month  / total_months 
#average_change = change_month / total_months *
    
result = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: $ {total_profit}\n"
    f"Average  Change: {average_change} \n"
    f"Greatest Increase in Profits: {max_month} $ {highest_increase}\n"
    f"Greatest Decrease in Profits: {min_month} $ {lowest_decrease}\n")
print(result)
# export into text file 
pybank = open ("python_challenge/PyBank/analysis/pybank.txt", "w")

pybank.write(result)
pybank.close()








   
