class SegmentTree:
    def __init__(self, arr):
        self.arr = arr.copy()
        self.n = len(self.arr)
        self.st = [0]*(4*self.n-1)
        self._build(1, 0, self.n-1)
    
    def _left(self, p):
        return 2*p
    
    def _right(self, p):
        return (2*p)+1
    
    def _build(self, p, L, R):
        if L==R:
            self.st[p]=L
        else:
            mid = (L+R)//2
            self._build(self._left(p), L, mid)
            self._build(self._right(p), mid+1, R)
            p1 = self.st[self._left(p)]
            p2 = self.st[self._right(p)]
            self.st[p] = p1 if self.arr[p1]<=self.arr[p2] else p2
    
    def _rmq(self, p, L, R, i, j):
        if i>R or j<L:
            return -1
        if L>=i and R<=j:
            return self.st[p]
    
        p1 = self._rmq(self._left(p), L, (L+R)//2, i, j)
        p2 = self._rmq(self._right(p), (L+R)//2+1, R, i, j)
        if p1==-1:
            return p2
        
        if p2==-1:
            return p1
        
        return p1 if self.arr[p1] <=self.arr[p2] else p2

    def rmq(self, i, j):
        return self._rmq(1, 0, self.n-1, i,j)
    
    def update_val(self, idx, new_val):
        if idx<0 or idx>=self.n:
            raise IndexError("Index out of bounds")
        
        self.arr[idx]=new_val
        self._update(1, 0, self.n-1, idx)
    
    def _update(self, p, L, R, idx):
        if L==R:
            return
        
        mid = (L+R)//2
        if idx<=mid:
            self._update(self._left(p), L, mid, idx)
        else:
            self._update(self._right(p), mid+1, R, idx)
        
        p1 = self.st[self._left(p)]
        p2 = self.st[self._right(p)]
        self.st[p] = p1 if self.arr[p1]<=self.arr[p2] else p2


if __name__=="__main__":
    arr = [18,17, 13,19,15,11,20]
    st = SegmentTree(arr)
    print(f"Original arry {arr}")
    print(f"RMQ(1, 3) = {st.rmq(1, 3)} (index {st.rmq(1, 3)} with value {arr[st.rmq(1, 3)]})")
    print(f"RMQ(0, 5) = {st.rmq(0, 5)} (index {st.rmq(0, 5)} with value {arr[st.rmq(0, 5)]})")
    print(f"RMQ(0, 0) = {st.rmq(0, 0)} (index {st.rmq(0, 0)} with value {arr[st.rmq(0, 0)]})")
    print(f"RMQ(4, 6) = {st.rmq(4, 6)} (index {st.rmq(4, 6)} with value {arr[st.rmq(4, 6)]})")
    print(f"RMQ(0, 50) = {st.rmq(0, 50)} (index {st.rmq(0, 50)} with value {arr[st.rmq(0, 50)]})")
    
    # Update value at index 5 from 11 to 99
    st.update_val(5, 1)
    print("\nAfter updating index 5 to 99:")
    print(f"Updated array: {st.arr}")
    print(f"RMQ(4, 6) = {st.rmq(4, 6)} (index {st.rmq(4, 6)} with value {st.arr[st.rmq(4, 6)]})")
