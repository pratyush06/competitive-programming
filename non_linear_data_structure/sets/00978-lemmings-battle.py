import heapq # it's min heap by default to use max heap negate the number(e.g -num for num )

def solve():
    num_of_test_cases = int(input())
    for tc in range(num_of_test_cases):
        if tc > 0:
            print()  # Blank line between test cases
        
        battle, num_greens, num_blue = map(int, input().split())
        green_heap = []
        blue_heap = []
        
        # Read green soldiers (use negative for max-heap)
        for _ in range(num_greens):
            heapq.heappush(green_heap, -int(input()))
        
        # Read blue soldiers (use negative for max-heap)
        for _ in range(num_blue):
            heapq.heappush(blue_heap, -int(input()))
        
        # Simulate battles
        while green_heap and blue_heap:
            current_battle = min(battle, len(green_heap), len(blue_heap))
            greens = []
            blues = []
            
            # Select soldiers for this round
            for _ in range(current_battle):
                greens.append(-heapq.heappop(green_heap))
                blues.append(-heapq.heappop(blue_heap))
            
            # Battle outcomes
            for g, b in zip(greens, blues):
                if g > b:
                    heapq.heappush(green_heap, -(g - b))
                elif b > g:
                    heapq.heappush(blue_heap, -(b - g))
        
        # Print results
        if not green_heap and not blue_heap:
            print("green and blue died")
        elif green_heap:
            print("green wins")
            for soldier in sorted((-x for x in green_heap), reverse=True):
                print(soldier)
        else:
            print("blue wins")
            for soldier in sorted((-x for x in blue_heap), reverse=True):
                print(soldier)

solve()