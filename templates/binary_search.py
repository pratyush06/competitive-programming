def first_true(left, right, predicate):
    """Return the first value in [left, right] where predicate(value) is True."""
    while left < right:
        mid = left + (right - left) // 2
        if predicate(mid):
            right = mid
        else:
            left = mid + 1
    return left


def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

