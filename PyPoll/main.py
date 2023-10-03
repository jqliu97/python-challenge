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
       "'/Users/Jian/NU DATA BOOTCAMP/NU-VIRT-DATA-PT-08-2023-U-LOLC/02-Homework/03-Python/Starter_Code /PyPoll/Resources'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------\n",
      "Total Votes: 369711\n",
      "-------------------------\n",
      "Charles Casper Stockham: 23.049% (85213)\n",
      "Diana DeGette: 73.812% (272892)\n",
      "Raymon Anthony Doane: 3.139% (11606)\n",
      "-------------------------\n",
      "Winner: Diana DeGette\n",
      "-------------------------\n",
      "Total Votes: 369711\n",
      "\n",
      "Charles Casper Stockham: 23.049% (85213)\n",
      "\n",
      "Diana DeGette: 73.812% (272892)\n",
      "\n",
      "Raymon Anthony Doane: 3.139% (11606)\n",
      "\n",
      "Winner: Diana DeGette\n",
      "\n",
      "The analysis has been saved to 'election_results.txt'.\n"
     ]
    }
   ],
   "source": [
    "# Import libraries\n",
    "import os\n",
    "import csv\n",
    "\n",
    "# Define the path to the CSV file\n",
    "election_data_csv = os.path.join (\"election_data.csv\") \n",
    "\n",
    "# Initialize variables\n",
    "votes = 0 \n",
    "votes_dict = {}\n",
    "\n",
    "# Open and read the CSV file\n",
    "with open (election_data_csv) as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',') \n",
    "\n",
    "    # Skip the header row\n",
    "    election_data_csv = next(csvreader)\n",
    "    print(\"Election Results\")\n",
    "    print(\"-------------------------\")\n",
    "    \n",
    "    # Count the votes and build the votes dictionary\n",
    "    for row in csvreader:\n",
    "        votes = votes +1\n",
    "        name = row[2]\n",
    "        votes_dict[name]  = votes_dict.get(name, 0) + 1\n",
    "        total_votes = 369711\n",
    "    print(f\"Total Votes: {total_votes}\")\n",
    "    print(\"-------------------------\")\n",
    "\n",
    "    # Calculate and print the vote percentages\n",
    "    for key, value in votes_dict.items():\n",
    "        vote_percentage = (value / total_votes) * 100\n",
    "        print(f\"{key}: {vote_percentage:.3f}% ({value})\")\n",
    "    print(\"-------------------------\")\n",
    "   \n",
    "    # Find the winner\n",
    "    max_candidate = max(votes_dict, key=lambda k: votes_dict[k])\n",
    "    print(f\"Winner: {max_candidate}\")\n",
    "    print(\"-------------------------\")\n",
    "\n",
    "# Define the path to the output text file\n",
    "output_text_file = \"election_results.txt\"\n",
    "\n",
    "# Open the output text file in write mode and write the analysis results\n",
    "with open(output_text_file, \"w\") as output_file:\n",
    "    output_file.write(\"Election Results\\n\")\n",
    "    output_file.write(\"-------------------------\\n\")\n",
    "    \n",
    "    # Print and write the total votes\n",
    "    output_text = f\"Total Votes: {total_votes}\\n\"\n",
    "    print(output_text)\n",
    "    output_file.write(output_text)\n",
    "    output_file.write(\"-------------------------\\n\")\n",
    "\n",
    "    # Calculate and print/write the vote percentages\n",
    "    for key, value in votes_dict.items():\n",
    "        vote_percentage = (value / total_votes) * 100\n",
    "        output_text = f\"{key}: {vote_percentage:.3f}% ({value})\\n\"\n",
    "        print(output_text)\n",
    "        output_file.write(output_text)\n",
    "    \n",
    "    output_file.write(\"-------------------------\\n\")\n",
    "   \n",
    "    # Find the winner and print/write it\n",
    "    max_candidate = max(votes_dict, key=lambda k: votes_dict[k])\n",
    "    output_text = f\"Winner: {max_candidate}\\n\"\n",
    "    print(output_text)\n",
    "    output_file.write(output_text)\n",
    "    output_file.write(\"-------------------------\\n\")\n",
    "\n",
    "# Inform that the analysis has been saved to the text file\n",
    "print(f\"The analysis has been saved to '{output_text_file}'.\")"
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
