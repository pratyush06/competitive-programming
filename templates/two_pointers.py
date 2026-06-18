def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


def merge_from_end(nums1, m, nums2, n):
    write = m + n - 1
    i, j = m - 1, n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1
        write -= 1

