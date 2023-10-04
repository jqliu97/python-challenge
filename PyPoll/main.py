# Import libraries
import os
import csv

# Define the path to the CSV file
election_data_csv = os.path.join ("election_data.csv") 

# Initialize variables
votes = 0 
votes_dict = {}

# Open and read the CSV file
with open (election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Skip the header row
    election_data_csv = next(csvreader)
    print("Election Results")
    print("-------------------------")
    
    # Count the votes and build the votes dictionary
    for row in csvreader:
        votes = votes +1
        name = row[2]
        votes_dict[name]  = votes_dict.get(name, 0) + 1
        total_votes = 369711
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # Calculate and print the vote percentages
    for key, value in votes_dict.items():
        vote_percentage = (value / total_votes) * 100
        print(f"{key}: {vote_percentage:.3f}% ({value})")
    print("-------------------------")
   
    # Find the winner
    max_candidate = max(votes_dict, key=lambda k: votes_dict[k])
    print(f"Winner: {max_candidate}")
    print("-------------------------")

# Define the path to the output text file
output_text_file = "election_results.txt"

# Open the output text file in write mode and write the analysis results
with open(output_text_file, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    
    # Print and write the total votes
    output_text = f"Total Votes: {total_votes}\n"
    print(output_text)
    output_file.write(output_text)
    output_file.write("-------------------------\n")

    # Calculate and print/write the vote percentages
    for key, value in votes_dict.items():
        vote_percentage = (value / total_votes) * 100
        output_text = f"{key}: {vote_percentage:.3f}% ({value})\n"
        print(output_text)
        output_file.write(output_text)
    
    output_file.write("-------------------------\n")
   
    # Find the winner and print/write it
    max_candidate = max(votes_dict, key=lambda k: votes_dict[k])
    output_text = f"Winner: {max_candidate}\n"
    print(output_text)
    output_file.write(output_text)
    output_file.write("-------------------------\n")

# Inform that the analysis has been saved to the text file
print(f"The analysis has been saved to '{output_text_file}'.")