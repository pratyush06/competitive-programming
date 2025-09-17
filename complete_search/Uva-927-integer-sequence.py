no_of_test_cases = int(input())
while no_of_test_cases > 0:
    cooefficient = list(input().split(" "))
    d = int(input())
    k = int(input())
    c0 = cooefficient[0]
    cooefficient = cooefficient[1:]
    group_no = None
    starting_pointer = 1
    pointer = 1
    while group_no is None:
        ending_pointer = starting_pointer + (d - 1)
        if k >= starting_pointer and k <= ending_pointer:
            group_no = pointer
        else:
            pointer += 1
            d += d
            starting_pointer = ending_pointer + 1

    ans = 0
    for i in range(0, len(cooefficient)):
        ans += int(cooefficient[i]) * (group_no) ** i
    
    ans += int(cooefficient[0])
    print(ans)
    no_of_test_cases -= 1