
import csv
total_months = 0
total_profit_loss_amount = 0.00
average_profit_loss = 0.00
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}
file_path = "./Resources/budget_data.csv"
with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        # The total number of months included in the dataset
        total_months = total_months + 1
        date = row[0]
        profit = float(row[1])
        # The net total amount of "Profit/Losses" over the entire period
<<<<<<< HEAD
        sum_profit = 0
        sum_loss = 0
        if profit > 0:
            sum_profit = sum_profit + profit
        elif profit <0:
            sum_loss = sum_loss + profit
        total_profit_loss_amount = sum_profit - sum_loss
            
=======

>>>>>>> cf1df046be2518b04d129361efd0c3fdb3cd3074
        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        # The greatest increase in profits (date and amount) over the entire period
        if (profit > greatest_increase["amount"]):
            greatest_increase["date"] = date
            greatest_increase["amount"] = profit
        # The greatest decrease in losses (date and amount) over the entire period
        if (profit < greatest_decrease["amount"]):
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = profit


# print results
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
<<<<<<< HEAD
print(f"Total: {total_profit_loss_amount}")
print("Average Change:")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
=======
print(
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
>>>>>>> cf1df046be2518b04d129361efd0c3fdb3cd3074
# results should look like
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
