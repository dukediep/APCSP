# 🐍 Python Portfolio

A collection of Python projects completed during CS50. Each project explores a different programming concept — from algorithms and simulations to data-driven applications.

---

### Project 1: Search Algorithm Comparison

**Summary**: Generates a random secret number between 1 and 100, then races two classic search algorithms to find it. Prints how many attempts each algorithm needed, making the performance difference immediately visible.

**Key Features**:
- Implements both Linear Search and Binary Search from scratch
- Demonstrates why Binary Search (O(log n)) is dramatically faster than Linear Search (O(n))
- Uses a shared random target so the comparison is always fair

---

### Project 2: Animal Race Simulation

**Summary**: Simulates 1000 races between a Tortoise, a Hare, and a Snail, each with unique movement rules and probabilities. Tracks win totals across all simulations and prints the final standings.

**Key Features**:
- Models real probability: the Hare is fast but has a 62.5% chance of falling asleep each turn
- The Snail has a wild card mechanic — it advances 13 meters but has a 90% chance of snapping back to the Hare's position
- Demonstrates how randomness and probability play out over large sample sizes (law of large numbers)

---

### Project 3: Dog Breed Finder

**Summary**: A menu-driven app that helps users find the right dog breed based on their lifestyle. Reads a real dog breed dataset using pandas and lets users filter by size, search by original purpose, or look up temperament info with a photo.

**Key Features**:
- Reads and processes a CSV dataset using the `pandas` library
- Four search modes: list all breeds, filter by size, search by purpose, or look up a specific breed
- Opens a photo of the selected breed in the browser using the `webbrowser` module
- Input validation and helpful error messages throughout

---

### Project 4: Peak Finder

**Summary**: Generates a random list of 12 integers and identifies every "peak" — a value that is strictly greater than its neighbors. Handles edge cases at both ends of the list correctly.

**Key Features**:
- Cleanly handles three cases: left edge, right edge, and middle elements
- Reports the index and value of every peak found
- Organized with a dedicated `find_peaks()` function and a `main()` entry point

---

### Project 5: Slot Machine

**Summary**: A fully interactive text-based slot machine where players deposit tokens, spin the reels, and collect payouts. Includes a hidden simulation mode that runs 1000 automated spins to reveal the house's statistical edge.

**Key Features**:
- Weighted random symbol selection — the rare `7` only appears 5% of the time
- Three payout tiers: Jackpot (200 tokens), Small Win (50 tokens), No Win
- Deposit system with valid amount checking (50, 100, or 500 tokens)
- Built-in `sim()` function that models the casino's long-run profit margin

---

## 🚀 How to Run

Each project is a standalone `.py` file. To run any of them:

```bash
python projects/search.py
python projects/race.py
python projects/peak.py
python projects/slotmachine.py
```

> **Note for `dogbreed.py`**: Requires a `dog.csv` file in the same directory and the `pandas` library installed (`pip install pandas`).

---

## 🛠️ Technologies Used

- Python 3
- `random` — built-in module for generating random numbers
- `pandas` — data analysis library for reading CSV files
- `webbrowser` — built-in module for opening URLs
