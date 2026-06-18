def subsets(nums):
    result = []
    path = []

    def dfs(start):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return result


def permutations(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def dfs():
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i, value in enumerate(nums):
            if used[i]:
                continue

            used[i] = True
            path.append(value)
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return result

