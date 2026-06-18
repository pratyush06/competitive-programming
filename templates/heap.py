import heapq


def k_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return sorted(heap, reverse=True)


def merge_sorted_lists(lists):
    heap = []
    result = []

    for list_index, values in enumerate(lists):
        if values:
            heapq.heappush(heap, (values[0], list_index, 0))

    while heap:
        value, list_index, value_index = heapq.heappop(heap)
        result.append(value)

        next_index = value_index + 1
        if next_index < len(lists[list_index]):
            next_value = lists[list_index][next_index]
            heapq.heappush(heap, (next_value, list_index, next_index))

    return result

