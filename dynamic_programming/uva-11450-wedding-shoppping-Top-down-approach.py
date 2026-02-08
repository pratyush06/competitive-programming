prices = []
C = None
M = None
memo = None
def place(money, i):
    return True if money-i>0 else False

def backtrack(money, garment):
    if memo[money][garment]!= None:
        return memo[money][garment]
    if money<0:
        return -1
    elif garment==C:
        return M-money
    ans = -float('inf')
    for i in prices[garment]:
        # print(i)
        if place(money, i):
            ans = max(ans, backtrack(money-i, garment+1))
    memo[money][garment]=ans
    return ans

def main():
    global prices, C, M, memo
    no_of_test_cases = int(input())
    for _ in range(no_of_test_cases):
        M, C = map(int, input().split(" "))
        for g in range(C):
            model = list(map(int, input().split(" ")))
            prices.append(model[1:])
        memo = [[None for _ in range(C+1)] for _ in range(M+1)]
        print(f"maximam amount person can spent is {backtrack(M, 0)}")


main()