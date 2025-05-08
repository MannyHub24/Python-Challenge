# -*- coding: UTF-8 -*-
"""PyBank Final Script."""

import csv
import os

# Update with your full path if needed
file_to_load = os.path.join("PyBank", "budget_data.csv")
file_to_output = os.path.join("PyBank", "financial_analysis.txt")

# Lists for tracking
months = []
profit_and_losses = []
p_l_changes = []

# Read CSV
with open(file_to_load, mode="r") as financial_data:
    csv_reader = csv.reader(financial_data)
    header = next(csv_reader)

    for row in csv_reader:
        months.append(row[0])
        profit_and_losses.append(int(row[1]))

# Calculations
total_months = len(months)
total_net = sum(profit_and_losses)

for i in range(1, len(profit_and_losses)):
    p_l_changes.append(profit_and_losses[i] - profit_and_losses[i - 1])

pl_avg_changes = round(sum(p_l_changes) / len(p_l_changes), 2)
greatest_increase_in_profits = max(p_l_changes)
greatest_decrease_in_profits = min(p_l_changes)

greatest_increase_month = months[p_l_changes.index(greatest_increase_in_profits) + 1]
greatest_decrease_month = months[p_l_changes.index(greatest_decrease_in_profits) + 1]

# Print summary
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${pl_avg_changes}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_in_profits})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_in_profits})")

# Write to file
with open(file_to_output, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_net}\n")
    file.write(f"Average Change: ${pl_avg_changes}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_in_profits})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_in_profits})\n")


