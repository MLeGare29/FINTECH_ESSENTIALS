"""Pathways to Success."""
# @TODO: Import the Path tool from the pathlib library
from pathlib import Path

# @TODO: Create a path to the `quarterly_data.csv` file
quarterly_data = Path("quarterly_data.csv")

# Print the relative path (the relative location of the file)
print(f"The relative CSV path is {quarterly_data}")

# Print the absolute path (The absolute location of the file on the computer)
print(f"The absolute CSV path is {quarterly_data.absolute()}")
