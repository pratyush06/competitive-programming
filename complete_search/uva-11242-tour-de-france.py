while True:
    no_of_clusters = list(map(int, input().split(" ")))
    if len(no_of_clusters)==1 and no_of_clusters[0]==0:
        break

    total_front_sp_cluster = no_of_clusters[0]
    rear_sp_clusters = no_of_clusters[1]

    no_of_front_teeth = list(map(int, input().split(" ")))
    no_of_rear_teeth = list(map(int, input().split(" ")))

    gear_spread = []
    for i in no_of_front_teeth:
        for j in no_of_rear_teeth:
            gear_spread.append(j/i)
    

    gear_spread.sort()

    spread = 0
    for i in range(len(gear_spread)-1):
        ratio = gear_spread[i+1]/gear_spread[i]
        if ratio>spread:
            spread=ratio

    print(f"{spread:.2f}")