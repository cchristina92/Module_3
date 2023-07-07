import csv 
import os

# Set the file path and text output
file_path = os.path.join("Resources", "election_data.csv")
text_path = os.path.join("analysis", "analysis_results.txt")

# Variables
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    
    header = next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:
        #total number of votes
        total_votes += 1
        candidate = row[2]

        # Increment the vote count 
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the results for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_results = (f"{candidate}: {percentage:.3f}% ({votes})")
    print(candidate_results)

    # winner with the most votes
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Open the output file in write mode
with open(text_path, "w") as file:
    
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    # Calculate results
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        # winner
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

# Print a message indicating the file was successfully created
print(f"Analysis results have been exported to {text_path}")
