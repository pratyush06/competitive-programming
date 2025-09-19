from itertools import combinations

while True:
    size_of_arr = int(input())
    if not size_of_arr:
        break
    Start = 0
    QUREY = 1
    
    arr =[]
    for _ in range(size_of_arr):
        arr.append(int(input()))
    
    all_combination = list(combinations(arr, 2))
    print(all_combination)
    sum_of_combinations = list(map(lambda t: t[0] + t[1], all_combination))
    events = [(x, Start) for x in sum_of_combinations]
    
    no_of_query = int(input())
    for _ in range(no_of_query):
        q = int(input())
        events.append((q, QUREY))
    
    events.sort()
    last_seen = None
    ans = []
    for idx, i in enumerate(events):
        if i[1]==Start:
            last_seen=i[0]
        elif i[1]==QUREY:
            closest_diff = abs(i[0]-last_seen) if last_seen is not None else None
            for k in range(idx+1, len(events)):
                if events[k][1]==Start:
                    if closest_diff is not None:
                        new_val = abs(events[k][0]-i[0])
                        if new_val<closest_diff:
                            ans.append(events[k][0])
                            break
                        else:
                            ans.append(last_seen)
                            break
                    
                    else:
                        ans.append(events[k][0])
                        break
                else:
                    continue
    
    print(ans)




    
