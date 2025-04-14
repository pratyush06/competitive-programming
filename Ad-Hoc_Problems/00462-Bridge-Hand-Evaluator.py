## Forgot to take care of malinformed card (edge condition) like length of input is lessa than 2 ref. line no 31

# ================== Handy Built-in Functions Cheat Sheet ==================

# ✅ all(iterable)
# Returns True if ALL elements in the iterable are True
# Useful for checking if all suits are "stopped", for example.
# Example:
# stopped = {'S': True, 'H': True, 'D': True, 'C': True}
# all(stopped.values()) → True

# ✅ any(iterable)
# Returns True if AT LEAST ONE element is True
# Example:
# any([False, False, True]) → True

# ✅ max(iterable, key=...)
# Finds the max element based on a custom key function
# - If values are tied, Python's max() returns the FIRST matching element (in original iterable order)
# - To break ties manually, return a tuple: (value, tie_breaker)
#   Tip: Use NEGATIVE index for tie-breaking when lower index = higher priority

# Example 1: Simple max using predefined suit order
types_of_card = ['S', 'H', 'D', 'C']
total_cards = {'S': 4, 'H': 4, 'D': 3, 'C': 2}
# Picks 'S' over 'H' because 'S' comes first in list
max_suit = max(types_of_card, key=lambda suit: total_cards[suit])

# Example 2: Custom tie-breaker using index
max_suit = max(types_of_card, key=lambda suit: (total_cards[suit], -types_of_card.index(suit)))
# - total_cards[suit] ensures highest count wins
# - -types_of_card.index(suit) gives preference to earlier suits in the list

# ===========================================================================

points_table = {
    'A': 4,
    'K': 3,
    'Q': 2,
    'J': 1
}
types_of_card = ['S', 'H', 'D', 'C']

while True:
    try:
        list_of_cards = input().split()
        if not list_of_cards:
            break

        total_points = 0
        total_sub_points = 0
        stopped_or_not = {suit: False for suit in types_of_card}
        total_cards = {suit: 0 for suit in types_of_card}

        # Count how many cards of each suit
        for card in list_of_cards:
            if len(card) < 2:
                continue  # Skip malformed cards
            suit = card[1]
            if suit in total_cards:
                total_cards[suit] += 1

        for card in list_of_cards:
            if len(card) < 2:
                continue
            rank, suit = card[0], card[1]

            # Add HCP
            total_points += points_table.get(rank, 0)

            # Handle stopped suits and deductions
            if rank == 'A':
                stopped_or_not[suit] = True
            elif rank == 'K':
                if total_cards[suit] == 1:
                    total_points -= 1
                else:
                    stopped_or_not[suit] = True
            elif rank == 'Q':
                if total_cards[suit] <= 2:
                    total_points -= 1
                else:
                    stopped_or_not[suit] = True
            elif rank == 'J':
                if total_cards[suit] <= 3:
                    total_points -= 1

        # Add distribution points
        for suit in types_of_card:
            count = total_cards[suit]
            if count == 2:
                total_sub_points += 1
            elif count == 1:
                total_sub_points += 2
            elif count == 0:
                total_sub_points += 2

        if all(stopped_or_not.values()) and total_points >= 16:
            print("BID NO-TRUMP")
        elif total_points + total_sub_points < 14:
            print("PASS")
        else:
            # Pick best suit (tie-breaking by order)
            max_suit = max(types_of_card, key=lambda s: total_cards[s])
            print(f"BID {max_suit}")
    except EOFError:
        break
