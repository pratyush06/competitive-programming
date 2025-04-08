while True:
    h,u,d,f = map(int, input().split())
    if not h:
        break
    else:
        distance_travelled=0
        fatigue_factor = round((f/100)*u, 2)
        count = 0
        while True:
            count+=1
            distance_travelled+=u
            if distance_travelled>h:
                print(f"success on day {count}")
                break
            distance_travelled-= d
            if distance_travelled<0:
                print(f"failure on day {count}")
                break
            u = max(0, u-fatigue_factor)

