"""
slotmachine.py
--------------
A text-based slot machine game with token deposits, spins, and payouts.
Includes a built-in simulation mode that runs 1000 spins automatically
to show the house's statistical edge over time.
"""

import random

# Slot machine symbols and their weighted probabilities
# Higher weight = more likely to appear
symbols = ["♠", "♡", "♢", "7"]
weights = [35, 35, 25, 5]   # 7 is rare (5%), suits are common (35/35/25%)

# Player's current token balance
player_credit = 0

print("Hello! Welcome to Slots")
print("Each spin costs 10 tokens")


def spin_reels():
    """
    Spins all three reels independently using weighted random selection.
    Returns a tuple of three single-symbol lists (r1, r2, r3).
    """
    r1 = random.choices(symbols, weights)
    r2 = random.choices(symbols, weights)
    r3 = random.choices(symbols, weights)
    return r1, r2, r3


def check_win(reels):
    """
    Checks if the three reels are a winning combination.

    Payouts:
      - Three 7s (JACKPOT): 200 tokens
      - Three matching suits: 50 tokens
      - No match: 0 tokens

    Returns a message string and the payout amount.
    """
    r1, r2, r3 = reels[0], reels[1], reels[2]

    if r1 == r2 and r2 == r3:
        if r1 == ["7"]:
            return "🎰 JACKPOT! Three 7s!", 200
        else:
            return "✨ Small Win! Three of a kind!", 50

    return "No win this time.", 0


def main():
    """
    Main game loop — lets the player deposit tokens, spin, or cash out.
    Each spin costs 10 tokens. The game ends when the player cashes out.
    """
    global player_credit

    while True:
        print("\n--- Slot Machine ---")
        print("1. Deposit tokens")
        print("2. Spin  (costs 10 tokens)")
        print("3. Cash out & exit")

        choice = input("Select 1, 2, or 3: ").strip()

        if choice == "1":
            amount = input("Deposit 50, 100, or 500 tokens: ").strip()
            if amount in ["50", "100", "500"]:
                player_credit += int(amount)
                print(f"Balance: {player_credit} tokens.")
            else:
                print("Invalid amount. Please enter 50, 100, or 500.")

        elif choice == "2":
            if player_credit < 10:
                print("Not enough tokens to spin. Please deposit more.")
            else:
                player_credit -= 10
                reels = spin_reels()
                # Display each reel's symbol cleanly
                display = f"[ {reels[0][0]} | {reels[1][0]} | {reels[2][0]} ]"
                print(f"\nSpin result: {display}")

                msg, payout = check_win(reels)
                print(msg)

                if payout > 0:
                    player_credit += payout
                    print(f"You won {payout} tokens!")

                print(f"Balance: {player_credit} tokens")

        elif choice == "3":
            print(f"\nThanks for playing! You cashed out with {player_credit} tokens.")
            break

        else:
            print("Invalid input. Please enter 1, 2, or 3.")


def sim():
    """
    Simulation mode: runs 1000 automated spins and reports the results.
    Useful for demonstrating the house edge built into the symbol weights.
    The house expects to profit because payouts are lower than true odds.
    """
    total_spent = 0
    total_won = 0

    for _ in range(1000):
        total_spent += 10  # Each spin costs 10 tokens

        # Spin three reels independently
        r1 = random.choices(symbols, weights)[0]
        r2 = random.choices(symbols, weights)[0]
        r3 = random.choices(symbols, weights)[0]

        # Check for a win
        if r1 == r2 == r3:
            if r1 == "7":
                total_won += 200  # Jackpot payout
            else:
                total_won += 50   # Small win payout

    print(f"\n--- 1000-Spin Simulation Results ---")
    print(f"Tokens Spent:    {total_spent}")
    print(f"Tokens Won:      {total_won}")
    print(f"House Profit:    {total_spent - total_won}")
    print(f"Player Return:   {round(total_won / total_spent * 100, 1)}%")


# Run the interactive game
main()

# Uncomment the line below to run the simulation instead:
# sim()
