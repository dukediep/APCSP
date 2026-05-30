"""
search.py
---------
Compares two classic search algorithms — Linear Search and Binary Search —
by finding a randomly generated secret number and counting how many attempts
each algorithm needs.
"""

import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
print(f"Secret Number: {secret_number}")


def linear_search(target):
    """
    Linear Search: checks every number from 1 to 100 in order.
    Worst case: 100 attempts. Average case: ~50 attempts.
    Simple but slow for large ranges.
    """
    attempts = 0
    for guess in range(1, 101):
        attempts += 1
        if guess == target:
            print(f"Linear Search: Found {target} in {attempts} attempts")
            break


def binary_search(target):
    """
    Binary Search: repeatedly cuts the search range in half.
    Worst case: ~7 attempts (log2 of 100). Much faster than linear search.
    Requires the search range to be sorted (1–100 already is).
    """
    attempts = 0
    low = 1
    high = 100
    found = False

    while not found:
        attempts += 1
        mid = (low + high) // 2  # Pick the middle of the current range

        if mid == target:
            print(f"Binary Search: Found {target} in {attempts} attempts")
            found = True
        elif mid < target:
            low = mid + 1   # Target must be in the upper half
        else:
            high = mid - 1  # Target must be in the lower half


# Run both searches on the same secret number
linear_search(secret_number)
binary_search(secret_number)
