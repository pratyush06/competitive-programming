## sweep line algorithm

def solve():
    db_length = int(input())
    events = []
    START = 0
    QUERY = 1
    END = 2
    for _ in range(db_length):
        car_maker, low_price, high_price = input().split(" ")
        events.append((int(low_price), START, car_maker))
        events.append((int(high_price), END, car_maker))
    quiries = int(input())
    for idx in range(quiries):
        q = int(input())
        events.append((q, QUERY, idx))
    
    available_car_makers = set()
    events.sort()
    answer = [""]*quiries
    for num, typ, idx in events:
        if typ==START:
            available_car_makers.add(idx)
        elif typ==END:
            available_car_makers.discard(idx)
        
        elif typ==QUERY:
            if len(available_car_makers)==1:
                answer[idx] = next(iter(available_car_makers))
            else:
                answer[idx] = "UNDETERMINED"
    
    print(f"answer: {answer}")



if __name__=="__main__":
    no_of_test_cases = int(input())
    for _ in range(no_of_test_cases):
        solve()