"""
dogbreed.py
-----------
Helps users find the right dog breed based on size or purpose.
Reads breed data from a CSV file and lets users browse breeds,
filter by size, search by purpose, or look up temperament info.

Data source: Provided by Mr. J
"""

import pandas as pd
import webbrowser

# Load the dog breed dataset from CSV
data = pd.read_csv('dog.csv')

# Extract relevant columns into lists for easy lookup
max_weight = data['Maximum Weight'].tolist()
min_weight = data['Minimum Weight'].tolist()
name = data['Name'].tolist()
temp = data['Temperament'].tolist()
image = data['Image'].tolist()
bred = data['BredFor'].tolist()

# Temporary list used to collect filtered results before printing
filtered = []


def size_finder(size):
    """
    Filters dog breeds by size category.
    Categories: tiny (≤10 lbs), small (11–25 lbs),
                medium (26–60 lbs), large (60+ lbs)
    """
    if size == "tiny":
        for i in range(len(max_weight)):
            if max_weight[i] <= 10:
                filtered.append(name[i])

    elif size == "small":
        for i in range(len(max_weight)):
            if max_weight[i] <= 25 and min_weight[i] >= 11:
                filtered.append(name[i])

    elif size == "medium":
        for i in range(len(max_weight)):
            if max_weight[i] <= 60 and min_weight[i] >= 26:
                filtered.append(name[i])

    elif size == "large":
        for i in range(len(max_weight)):
            if max_weight[i] >= 60:
                filtered.append(name[i])

    else:
        print("Invalid size. Choose: tiny, small, medium, or large.")
        return

    if filtered:
        print("Matching breeds:", filtered)
    else:
        print("No breeds found for that size.")

    filtered.clear()


def info(breed_name):
    """
    Displays the temperament of a specific breed
    and opens its image in the default web browser.
    """
    found = False
    for i in range(len(name)):
        if name[i].lower() == breed_name.lower():
            print(f"Temperament: {temp[i]}")
            webbrowser.open(image[i])
            found = True
            break
    if not found:
        print(f"Breed '{breed_name}' not found. Check the spelling.")


def purp(purpose):
    """
    Finds breeds that were originally bred for a given purpose
    (e.g., 'hunting', 'herding', 'companionship').
    """
    for i in range(len(bred)):
        # Check if the purpose keyword appears in the breed's purpose description
        if isinstance(bred[i], str) and purpose in bred[i].lower():
            filtered.append(name[i])

    if filtered:
        print("Matching breeds:", filtered)
        filtered.clear()
    else:
        print("No breeds found for that purpose.")


def menu():
    """
    Main menu loop — lets the user choose what to search for
    and calls the appropriate function.
    """
    while True:
        print("\n--- Dog Breed Finder ---")
        print("1. List all breeds")
        print("2. Find dog by size")
        print("3. Find dog by purpose")
        print("4. Look up breed temperament")
        print("5. Exit")

        user = input("Please select 1–5: ").strip()

        if user == "1":
            print("All breeds:", name)

        elif user == "2":
            size = input("What size? (tiny, small, medium, large): ").lower().strip()
            size_finder(size)

        elif user == "3":
            print("Example purposes:", bred[:5])  # Show a few examples to guide the user
            purpose = input("What purpose are you looking for? ").lower().strip()
            purp(purpose)

        elif user == "4":
            breed_name = input("Enter the breed name: ").strip()
            info(breed_name)

        elif user == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number from 1 to 5.")


# Run the program
menu()
