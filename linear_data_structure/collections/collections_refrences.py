# Python Collections Module Reference
# A guide to key data structures in the collections module for competitive programming
# Last updated: June 12, 2025

from collections import Counter, deque, defaultdict, OrderedDict, namedtuple
from typing import List, Tuple, Dict, Any

# 1. Counter: Counts hashable objects (like a frequency map)
def counter_examples():
    """Demonstrates Counter usage for frequency counting."""
    # Example 1: Count frequencies in a list
    arr = [1, 2, 2, 3, 1, 1, 4]
    freq = Counter(arr)
    print(f"Counter frequencies: {freq}")  # Counter({1: 3, 2: 2, 3: 1, 4: 1})
    
    # Access count
    print(f"Count of 1: {freq[1]}")  # 3
    
    # Non-existent element (returns 0, no KeyError)
    print(f"Count of 5: {freq[5]}")  # 0
    
    # Example 2: Most common elements
    most_common = freq.most_common(2)  # Top 2 elements by frequency
    print(f"Most common: {most_common}")  # [(1, 3), (2, 2)]
    
    # Example 3: Counter with strings
    s = "programming"
    char_freq = Counter(s)
    print(f"Character frequencies: {char_freq}")  # Counter({'g': 2, 'r': 2, ...})
    
    # Example 4: Counter arithmetic
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2)
    print(f"Sum: {c1 + c2}")  # Counter({'a': 4, 'b': 3})
    print(f"Difference: {c1 - c2}")  # Counter({'a': 2})

# 2. deque: Double-ended queue for fast appends/pops from both ends
def deque_examples():
    """Demonstrates deque usage for queue and stack operations."""
    # Initialize deque
    dq = deque([1, 2, 3])
    print(f"Initial deque: {dq}")  # deque([1, 2, 3])
    
    # Append to right
    dq.append(4)
    print(f"After append(4): {dq}")  # deque([1, 2, 3, 4])
    
    # Append to left
    dq.appendleft(0)
    print(f"After appendleft(0): {dq}")  # deque([0, 1, 2, 3, 4])
    
    # Pop from right
    right = dq.pop()
    print(f"Popped right: {right}, deque: {dq}")  # 4, deque([0, 1, 2, 3])
    
    # Pop from left
    left = dq.popleft()
    print(f"Popped left: {left}, deque: {dq}")  # 0, deque([1, 2, 3])
    
    # Example: Sliding window maximum
    def sliding_window_max(arr: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        for i in range(len(arr)):
            # Remove elements outside window
            if dq and dq[0] <= i - k:
                dq.popleft()
            # Remove smaller elements from back
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(arr[dq[0]])
        return result
    
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Sliding window max (k={k}): {sliding_window_max(arr, k)}")

# 3. defaultdict: Dictionary with default values for missing keys
def defaultdict_examples():
    """Demonstrates defaultdict for avoiding KeyError."""
    # Initialize with int (default 0)
    d = defaultdict(int)
    
    # Count frequencies without checking keys
    arr = [1, 2, 2, 1, 3]
    for x in arr:
        d[x] += 1
    print(f"Frequency dict: {dict(d)}")  # {1: 2, 2: 2, 3: 1}
    
    # Example: Group by length
    words = ["cat", "dog", "rat", "deer"]
    group = defaultdict(list)
    for w in words:
        group[len(w)].append(w)
    print(f"Grouped by length: {dict(group)}")  # {3: ['cat', 'dog', 'rat'], 4: ['deer']}
    
    # Custom default_factory
    d = defaultdict(lambda: -1)
    d["a"] = 10
    print(f"Value of 'a': {d['a']}, 'b': {d['b']}")  # 10, -1

# 4. OrderedDict: Dictionary that remembers insertion order
def ordereddict_examples():
    """Demonstrates OrderedDict for order-sensitive operations."""
    # Note: Since Python 3.7, regular dict preserves order, but OrderedDict has extras
    od = OrderedDict()
    od["apple"] = 3
    od["banana"] = 1
    od["orange"] = 2
    print(f"OrderedDict: {od}")  # OrderedDict([('apple', 3), ('banana', 1), ('orange', 2)])
    
    # Move to end
    od.move_to_end("apple")
    print(f"After move_to_end('apple'): {od}")
    
    # Pop item
    key, value = od.popitem(last=False)  # Pop from start
    print(f"Popped: ({key}, {value}), OrderedDict: {od}")
    
    # Example: LRU Cache implementation
    class LRUCache:
        def __init__(self, capacity: int):
            self.cache = OrderedDict()
            self.capacity = capacity
        
        def get(self, key: int) -> int:
            if key not in self.cache:
                return -1
            self.cache.move_to_end(key)
            return self.cache[key]
        
        def put(self, key: int, value: int) -> None:
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
    
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"Get 1: {cache.get(1)}")  # 1
    cache.put(3, 3)  # Evicts key 2
    print(f"Get 2: {cache.get(2)}")  # -1

# 5. namedtuple: Lightweight object type with named fields
def namedtuple_examples():
    """Demonstrates namedtuple for structured data."""
    # Define namedtuple
    Point = namedtuple("Point", ["x", "y"])
    
    # Create instance
    p = Point(1, 2)
    print(f"Point: {p}, x: {p.x}, y: {p.y}")  # Point(x=1, y=2), x: 1, y: 2
    
    # Unpack
    x, y = p
    print(f"Unpacked: x={x}, y={y}")  # x=1, y=2
    
    # Example: Store and sort points
    points = [Point(1, 2), Point(3, 1), Point(2, 3)]
    sorted_points = sorted(points, key=lambda p: p.y, reverse=True)
    print(f"Sorted by y: {sorted_points}")  # [Point(x=3, y=1), Point(x=1, y=2), Point(x=2, y=3)]

# Main function to run all examples
def main():
    print("=== Collections Module Reference ===")
    print("\n1. Counter Examples")
    counter_examples()
    print("\n2. deque Examples")
    deque_examples()
    print("\n3. defaultdict Examples")
    defaultdict_examples()
    print("\n4. OrderedDict Examples")
    ordereddict_examples()
    print("\n5. namedtuple Examples")
    namedtuple_examples()

if __name__ == "__main__":
    main()

# Competitive Programming Tips:
# - Use Counter for frequency-based problems (e.g., anagrams, majority element).
# - Use deque for sliding window, BFS, or stack/queue operations.
# - Use defaultdict to simplify dictionary initialization (e.g., grouping, counting).
# - Use OrderedDict for order-sensitive problems like LRU Cache (less common since dict order preserved in Python 3.7+).
# - Use namedtuple for lightweight structs to improve code clarity.
# - Time complexities:
#   - Counter: O(n) to build, O(1) access.
#   - deque: O(1) for append/pop from ends.
#   - defaultdict: Same as dict, O(1) average case.
#   - OrderedDict: O(1) for most operations, including move_to_end.
#   - namedtuple: O(1) access, immutable.