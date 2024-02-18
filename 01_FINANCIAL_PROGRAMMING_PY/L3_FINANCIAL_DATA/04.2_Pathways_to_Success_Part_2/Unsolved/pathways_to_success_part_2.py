"""Pathways to Success Part 2."""
# @TODO: Import the csv library
import csv
from pathlib import Path

# @TODO: Create a path to the csv file called `quarterly_data.csv`
quarterly_data = Path("quarterly_data.csv")

# @TODO: Open the csv path, read the data, and print each row
with open(quarterly_data) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)

"""Extension.

This is an optional extension to the activity.

Create a variable above the `for` loop named `Counter`
and set it equal to zero. Then, every time a new row
is read within the `for` loop, add a value of 1 to
this variable.
"""

# @TODO: Add a row counter to the CSV data.
quarterly_data = Path("quarterly_data.csv")
counter = 0
with open(quarterly_data) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        # For every new row, add 1 `counter`
        counter = counter + 1
        # Print the row counter and then the row
        print(f"Row Counter {counter}")
        print(row)
        
