def fibonacci_top_down(n):
    memo = {}

    def dp(i):
        if i <= 1:
            return i
        if i not in memo:
            memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]

    return dp(n)


def knapsack_01(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for cap in range(capacity, weight - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - weight] + value)

    return dp[capacity]


def longest_increasing_subsequence_length(nums):
    tails = []

    for num in nums:
        left, right = 0, len(tails)
        while left < right:
            mid = left + (right - left) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid

        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num

    return len(tails)

