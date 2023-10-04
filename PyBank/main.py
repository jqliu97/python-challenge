# Import libraries
import os
import csv

# Define path to CSV file
budget_data_csv = os.path.join("Resources","budget_data.csv") 

# Initialize variables
total_months = 0
net_total = 0
previous_net = 0
changes = []

greatest_increase_amount = 0
greatest_decrease_amount = 0
greatest_increase_month = ""
greatest_decrease_month = ""

# Open and read CSV file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Skip header row
    budget_data_csv = next(csvreader)
    print(f"Header: {budget_data_csv}")

    # Read profit/loss for first month
    firstrow = next(csvreader)
    previous_net = int(firstrow[1])

    # Update total months and net total
    total_months += 1
    net_total += int(firstrow[1])

    # Iterate through remaining rows
    for row in csvreader:
        
        # Calculate net change in profit/loss
        net_change = int(row[1]) - previous_net
        
        # Update net total, total months, and previous net
        net_total += int(row[1])
        total_months += 1
        previous_net = int(row[1])
        
        # Store net change in 'changes' list
        changes = changes + [net_change]

        # Check for greatest increase in profit/loss and associated month
        if net_change > greatest_increase_amount:
           greatest_increase_amount = net_change
           greatest_increase_month = row[0]    

        # Check for greatest decrease in profit/loss and associated month
        if net_change < greatest_decrease_amount:
            greatest_decrease_amount = net_change
            greatest_decrease_month = row[0]

# Calculate average change
avg = round(sum(changes) / len(changes),2)

# Print header
print("Financial Analysis")
print("---------------------------")

# Print total months
print(f"Total Months: {total_months}")

# Print net total
print(f"Total: ${net_total}")

# Print average change
print(f"Average Change: ${avg}")

# Print greatest increase 
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})")

# Print greatest decrease
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})")

# Define the path to the output text file
output_text_file = "budget_analysis.txt"

# Open the output text file in write mode and write the analysis results
with open(output_text_file, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("---------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${avg}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})\n")

# Inform that the analysis has been saved to the text file
print(f"The analysis has been saved to '{output_text_file}'.")