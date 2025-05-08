# PyPoll - Super Beginner Friendly Version

# This program counts votes from a CSV file and figures out who won the election

import csv  # Let's us read .csv files
import os   # Helps us work with file paths and folders

# This is where the vote data is saved (you can change the path if needed)
file_to_load = os.path.join("PyPoll", "election_data.csv")

# This is where we want to save the results
file_to_output = os.path.join("PyPoll", "election_analysis.txt")

# Start with 0 total votes
total_votes = 0

# Make an empty dictionary to keep track of each candidate's votes
candidate_votes = {}

# Open the vote file and read the data
with open(file_to_load, "r") as file:
    reader = csv.reader(file)

    # Skip the first row since it just has column titles
    header = next(reader)

    # Go through every row in the file
    for row in reader:
        total_votes = total_votes + 1  # Add one to the total vote count

        # The candidate's name is in the third column (index 2)
        name = row[2]

        # If we've seen this candidate before, add 1 to their vote count
        if name in candidate_votes:
            candidate_votes[name] = candidate_votes[name] + 1
        else:
            # If it's the first time seeing this name, start their count at 1
            candidate_votes[name] = 1

# Figure out which candidate got the most votes
winner = max(candidate_votes, key=candidate_votes.get)

# Now make a list of results we want to show and save
results = []
results.append("Election Results")
results.append("-------------------------")
results.append("Total Votes: " + str(total_votes))
results.append("-------------------------")

# Add each candidate's name, vote count, and percentage
for name in candidate_votes:
    votes = candidate_votes[name]
    percent = (votes / total_votes) * 100
    results.append(name + ": " + str(round(percent, 3)) + "% (" + str(votes) + ")")

# Add the winner to the results
results.append("-------------------------")
results.append("Winner: " + winner)
results.append("-------------------------")

# Print everything to the screen
print("\nHere are the results:\n")
for line in results:
    print(line)

# Save the results in a text file
with open(file_to_output, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for name in candidate_votes:
        votes = candidate_votes[name]
        percent = (votes / total_votes) * 100
        file.write(f"{name}: {round(percent, 3)}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")


