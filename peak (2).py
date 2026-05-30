"""
peak.py
-------
Generates a list of 12 random integers and identifies all "peaks" —
values that are strictly greater than their neighbors.

A peak at the edge only needs to beat one neighbor.
A peak in the middle must beat both neighbors.
"""

import random


def find_peaks(data):
    """
    Scans a list and prints the index and value of every peak.

    A peak is defined as:
      - First element: greater than the next element
      - Last element: greater than the previous element
      - Middle elements: greater than both neighbors
    """
    print("Peaks found:")
    peak_count = 0

    for i in range(len(data)):
        if i == 0:
            # Left edge: only compare to the right neighbor
            if data[i] > data[i + 1]:
                print(f"  Peak at index {i}: {data[i]}")
                peak_count += 1

        elif i == len(data) - 1:
            # Right edge: only compare to the left neighbor
            if data[i] > data[i - 1]:
                print(f"  Peak at index {i}: {data[i]}")
                peak_count += 1

        else:
            # Middle: must beat both neighbors
            if data[i] > data[i - 1] and data[i] > data[i + 1]:
                print(f"  Peak at index {i}: {data[i]}")
                peak_count += 1

    if peak_count == 0:
        print("  No peaks found.")


def main():
    # Generate 12 random integers between 0 and 50
    data = [random.randint(0, 50) for _ in range(12)]
    print("Data:", data)
    print()
    find_peaks(data)


main()
