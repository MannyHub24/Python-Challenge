# PyPoll - Election Results

## Overview

This Python script was created to help a small, rural town modernize its vote-counting process by analyzing a large dataset of election results. The data is stored in a CSV file containing the following columns:

- **Voter ID**
- **County**
- **Candidate**

The script calculates the following election metrics:

- Total number of votes casted.
- Complete list of candidates who received votes.
- Total and percentage of votes each candidate won.
- Winner of the election based on popular vote.

## Dataset

- File name: `election_data.csv`
- Number of rows: 369,712 (including header).
- Location: Local directory.

## Technologies Used

- Python 
- `csv` module
- `os` module

## How to Run

1. Make sure you have Python installed on your machine.
2. Place the `election_data.csv` file in the same directory as the Python script.
3. Run the script in your terminal or code editor:
   ```bash
   python main.py
   ```

## Output Example

```
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```

## Notes

- The script uses a dictionary to count votes for each candidate.
- Percentages are calculated to three decimal places.
- Winner is determined based on the highest total votes.
- Output is printed in the terminal and also saved as a `.txt` file in the same folder.

## Author

Manuel Guevara
