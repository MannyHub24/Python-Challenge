# PyBank - Financial Analysis

## Overview

This Python script analyzes the financial records of a company to produce a summary of key financial metrics. The dataset contains monthly profit/loss figures and is stored in a CSV file with the following columns:

- **Date** (e.g., Jan-2010)
- **Profit/Losses** (e.g., 867884)

The script calculates:

- Total number of months included in the dataset.
- Net total amount of Profit/Losses over the entire period.
- Average change in Profit/Losses between months.
- Greatest increase in profits (date and amount).
- Greatest decrease in profits (date and amount).

## Dataset

- File name: `budget_data.csv`
- Number of rows: varies by dataset.
- Location: `PyBank` folder within the project directory.

## Technologies Used

- Python
- `csv` module
- `os` module

## How to Run

1. Ensure Python is installed on your machine.
2. Place the `budget_data.csv` file inside a folder in the same directory as the script.
3. Run the script in a terminal or code editor:
   ```bash
   python main.py
   ```

## Output Example

```
Financial Analysis
-------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```

## Notes

- The script uses lists to store and compute monthly changes.
- Output is printed in the terminal and also saved as a `.txt` file in the same folder.
- File and folder paths may be customized as needed.

## Author

Manuel Guevara
