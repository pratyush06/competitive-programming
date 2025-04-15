# mistake I did here was missed the line which says input is provided in bottom to top order

no_of_test = int(input())

for i in range(1, no_of_test+1):
    Y = 0
    orders_of_cards = list(input().split())
    orders_of_cards = orders_of_cards[::-1] # reversed the order since input is bottom to top
    top_25 = orders_of_cards[:25]
    remaining_cards = orders_of_cards[25:]
    for j in range(3):
        top_value = remaining_cards[0][0]
        if top_value in ["K", "J", "Q", "A", "T"]:
            Y+=10
            remaining_cards = remaining_cards[1:]
        else:
            Y+=int(top_value)
            remaining_cards = remaining_cards[1:]
            remaining_cards  = remaining_cards[(10-int(top_value)):]
    
    total_cards = top_25 + remaining_cards
    ans = total_cards[-Y]
    print(f"Case {i}: {ans}")