# Python Challenge - PyBank and PyPoll

## Overview

This assignment contains two Python scripts created to perform data analysis tasks on financial and election datasets as part of a Python programming challenge.

---

## Part 1: PyBank - Financial Analysis

This script analyzes the financial records of a company to produce a summary of key financial metrics. The dataset contains monthly profit/loss figures and is stored in a CSV file with the following columns:

- **Date** (e.g., Jan-2010)
- **Profit/Losses** (e.g., 867884)

### The script calculates:

- Total number of months included in the dataset.
- Net total amount of Profit/Losses over the entire period.
- Average change in Profit/Losses between months.
- Greatest increase in profits (date and amount).
- Greatest decrease in profits (date and amount).

### Dataset

- File name: `budget_data.csv`
- Location: `PyBank` folder

### Technologies Used

- Python
- `csv` module
- `os` module

### How to Run

1. Ensure Python is installed on your machine.
2. Place `budget_data.csv` inside a `Resources` folder within the PyBank project directory.
3. Run the script in a terminal or editor:
   ```bash
   python pybank.py
   ```

### Output Example

```
Financial Analysis
-------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```

---

## Part 2: PyPoll - Election Results

This script was created to help a rural town modernize its vote-counting process by analyzing a large dataset of election results stored in a CSV file with the following columns:

- **Voter ID**
- **County**
- **Candidate**

### The script calculates:

- Total number of votes cast.
- Complete list of candidates who received votes.
- Total and percentage of votes each candidate won.
- Winner of the election based on popular vote.

### Dataset

- File name: `election_data.csv`
- Location: `PyPoll` folder

### Technologies Used

- Python
- `csv` module
- `os` module

### How to Run

1. Ensure Python is installed on your machine.
2. Place `election_data.csv` in the `Resources` folder within the PyPoll directory.
3. Run the script in a terminal or editor:
   ```bash
   python pypoll.py
   ```

### Output Example

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

---

## Notes

- Both scripts output the results to the terminal and save them in `.txt` files inside their original folder.
- PyBank uses lists and loop logic to compute changes in financial data.
- PyPoll uses a dictionary to tally votes and determine election results.

## Author

Manuel Guevara
