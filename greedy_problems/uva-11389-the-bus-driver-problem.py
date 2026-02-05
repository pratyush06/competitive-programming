list_of_input = list(map(int, input().split()))
n, d, r = list_of_input[0], list_of_input[1], list_of_input[2]
length_of_morning_routes = list(map(int, input().split()))
length_of_night_routes = list(map(int, input().split()))
length_of_morning_routes.sort(reverse=True)
total_cost = 0
for i, j in zip(length_of_morning_routes, length_of_night_routes):
    if (i+j)>d:
        extra_hrs=((i+j)-d)
        total_cost+=(extra_hrs*r)

print(total_cost)