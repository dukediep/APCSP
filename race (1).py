"""
race.py
-------
Simulates 1000 races between a Tortoise, a Hare, and a Snail.
Each racer has unique movement rules and probabilities.
Tracks how many races each animal wins and prints the final totals.
"""

import random

# Win counters for each racer
tortoise_wins = 0
hare_wins = 0
snail_wins = 0

# Run 1000 race simulations
for i in range(1000):
    finish_line = 50   # Distance needed to win
    tortoise_pos = 0   # Starting position for tortoise
    hare_pos = 0       # Starting position for hare
    snail_pos = 0      # Starting position for snail
    is_hare_asleep = False  # Hare begins each race awake

    # Simulate one race — loop until any racer crosses the finish line
    while tortoise_pos < finish_line and hare_pos < finish_line and snail_pos < finish_line:

        # Tortoise: steady and consistent, moves 1–3 meters each turn
        tortoise_move = random.randint(1, 3)
        tortoise_pos += tortoise_move

        # Hare: 62.5% chance of falling asleep each turn
        if random.random() < 0.625:
            is_hare_asleep = True
        else:
            is_hare_asleep = False

        # If the hare is awake, it moves fast (1–10 meters)
        if not is_hare_asleep:
            hare_move = random.randint(1, 10)
            hare_pos += hare_move

        # Snail: moves 13 meters but has a 90% chance of being
        # pushed back to the hare's current position (shell shock!)
        snail_pos += 13
        if random.random() < 0.9:
            snail_pos = hare_pos

    # Determine winner of this race
    if tortoise_pos >= finish_line:
        tortoise_wins += 1
    elif hare_pos >= finish_line:
        hare_wins += 1
    else:
        snail_wins += 1

# Print final race results after all 1000 simulations
print(f"Results after 1000 races:")
print(f"  Tortoise wins: {tortoise_wins}")
print(f"  Hare wins:     {hare_wins}")
print(f"  Snail wins:    {snail_wins}")
