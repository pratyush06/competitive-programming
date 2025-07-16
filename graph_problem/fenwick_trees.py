class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.ft = [0] * (n + 2)  # 1-based indexing

    def lsone(self, s):
        return s & (-s)

    def rsq(self, b):
        res = 0
        while b > 0:
            res += self.ft[b]
            b -= self.lsone(b)
        return res

    def rsq_range(self, a, b):
        return self.rsq(b) - (0 if a == 1 else self.rsq(a - 1))

    def adjust(self, k, v):
        while k <= self.size:
            self.ft[k] += v
            k += self.lsone(k)

if __name__ == "__main__":
    f = [2, 4, 5, 5, 6, 6, 6, 7, 7, 8, 9]
    ft = FenwickTree(10)  # Range [1..10]
    
    # Insert scores
    for num in f:
        ft.adjust(num, 1)
    
    # Test queries
    print(ft.rsq_range(1, 1))   # 0
    print(ft.rsq_range(1, 2))   # 1
    print(ft.rsq_range(1, 6))   # 7
    print(ft.rsq_range(1, 10))  # 11
    print(ft.rsq_range(3, 6))   # 6
    
    # Update and test
    ft.adjust(5, 2)
    print(ft.rsq_range(1, 10))  # 13