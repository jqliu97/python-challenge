{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/Jian/NU DATA BOOTCAMP/NU-VIRT-DATA-PT-08-2023-U-LOLC/02-Homework/03-Python/Starter_Code /PyBank'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Header: ['Date', 'Profit/Losses']\n",
      "Financial Analysis\n",
      "---------------------------\n",
      "Total Months: 86\n",
      "Total: $22564198\n",
      "Average Change: $-8311.11\n",
      "Greatest Increase in Profits: Aug-16 ($1862002)\n",
      "Greatest Decrease in Profits: Feb-14 ($-1825558)\n",
      "The analysis has been saved to 'budget_analysis.txt'.\n"
     ]
    }
   ],
   "source": [
    "# Import libraries\n",
    "import os\n",
    "import csv\n",
    "\n",
    "# Define path to CSV file\n",
    "budget_data_csv = os.path.join(\"Resources\",\"budget_data.csv\") \n",
    "\n",
    "# Initialize variables\n",
    "total_months = 0\n",
    "net_total = 0\n",
    "previous_net = 0\n",
    "changes = []\n",
    "\n",
    "greatest_increase_amount = 0\n",
    "greatest_decrease_amount = 0\n",
    "greatest_increase_month = \"\"\n",
    "greatest_decrease_month = \"\"\n",
    "\n",
    "# Open and read CSV file\n",
    "with open(budget_data_csv) as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',') \n",
    "\n",
    "    # Skip header row\n",
    "    budget_data_csv = next(csvreader)\n",
    "    print(f\"Header: {budget_data_csv}\")\n",
    "\n",
    "    # Read profit/loss for first month\n",
    "    firstrow = next(csvreader)\n",
    "    previous_net = int(firstrow[1])\n",
    "\n",
    "    # Update total months and net total\n",
    "    total_months += 1\n",
    "    net_total += int(firstrow[1])\n",
    "\n",
    "    # Iterate through remaining rows\n",
    "    for row in csvreader:\n",
    "        \n",
    "        # Calculate net change in profit/loss\n",
    "        net_change = int(row[1]) - previous_net\n",
    "        \n",
    "        # Update net total, total months, and previous net\n",
    "        net_total += int(row[1])\n",
    "        total_months += 1\n",
    "        previous_net = int(row[1])\n",
    "        \n",
    "        # Store net change in 'changes' list\n",
    "        changes = changes + [net_change]\n",
    "\n",
    "        # Check for greatest increase in profit/loss and associated month\n",
    "        if net_change > greatest_increase_amount:\n",
    "           greatest_increase_amount = net_change\n",
    "           greatest_increase_month = row[0]    \n",
    "\n",
    "        # Check for greatest decrease in profit/loss and associated month\n",
    "        if net_change < greatest_decrease_amount:\n",
    "            greatest_decrease_amount = net_change\n",
    "            greatest_decrease_month = row[0]\n",
    "\n",
    "# Calculate average change\n",
    "avg = round(sum(changes) / len(changes),2)\n",
    "\n",
    "# Print header\n",
    "print(\"Financial Analysis\")\n",
    "print(\"---------------------------\")\n",
    "\n",
    "# Print total months\n",
    "print(f\"Total Months: {total_months}\")\n",
    "\n",
    "# Print net total\n",
    "print(f\"Total: ${net_total}\")\n",
    "\n",
    "# Print average change\n",
    "print(f\"Average Change: ${avg}\")\n",
    "\n",
    "# Print greatest increase \n",
    "print(f\"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})\")\n",
    "\n",
    "# Print greatest decrease\n",
    "print(f\"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})\")\n",
    "\n",
    "# Define the path to the output text file\n",
    "output_text_file = \"budget_analysis.txt\"\n",
    "\n",
    "# Open the output text file in write mode and write the analysis results\n",
    "with open(output_text_file, \"w\") as output_file:\n",
    "    output_file.write(\"Financial Analysis\\n\")\n",
    "    output_file.write(\"---------------------------\\n\")\n",
    "    output_file.write(f\"Total Months: {total_months}\\n\")\n",
    "    output_file.write(f\"Total: ${net_total}\\n\")\n",
    "    output_file.write(f\"Average Change: ${avg}\\n\")\n",
    "    output_file.write(f\"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})\\n\")\n",
    "    output_file.write(f\"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})\\n\")\n",
    "\n",
    "# Inform that the analysis has been saved to the text file\n",
    "print(f\"The analysis has been saved to '{output_text_file}'.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
