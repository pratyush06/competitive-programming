# complexity of the problem is O(n^2) but it will pass the test since length can me of maximum 1000 so in worst case it can be 10^6
# general rule of thumb to identify if n^2 or complete search problem will pass or not is in worst case it should take less than 10^8 time
def solve():
    length_of_arr = int(input())
    arr = list(map(int, input().split(" ")))
    sum_of_b = 0
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i]>=arr[j]:
                sum_of_b+=1
    
    print(sum_of_b)


if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        solve()
