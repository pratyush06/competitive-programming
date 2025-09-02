class PirateSegmentTree:
    def __init__(self, pirates):
        self.n = len(pirates)
        self.pirates_list = list(pirates)
        self.st = [0]*(4*self.n-1)
        # import pdb;pdb.set_trace()
        self._build(1, 0, self.n-1)
    
    def _left(self, p):
        return 2*p
    def _right(self, p):
        return (2*p)+1
    
    def _build(self, p, L, R):
        if L==R:
            # import pdb;pdb.set_trace()
            self.st[p]=int(self.pirates_list[L])
        else:
            mid = (L+R)//2
            self._build(self._left(p), L, mid)
            self._build(self._right(p), mid+1, R)
            p1 = self.st[self._left(p)]
            p2 = self.st[self._right(p)]
            self.st[p] = p1+p2
    
    def update_val(self,type_of_op, start, end):
        if type_of_op=='F':
            for i in range(start, end+1):
                self.pirates_list[i]='1'
        elif type_of_op=='E':
            for i in range(start, end+1):
                self.pirates_list[i]='0'
        elif type_of_op=='I':
            for i in range(start, end+1):
                if self.pirates_list[i]=='1':
                    self.pirates_list[i]='0'
                else:
                    self.pirates_list[i]='1'
        else:
            return
        self.update(1, 0, self.n-1, start, end)
    def update(self,p, L, R, start, end):
        # import pdb;pdb.set_trace()
        if start>R or end<L:
            return
        if L==R:
            self.st[p]=int(self.pirates_list[L])
            return
        mid = (L+R)//2
        # if L=>start and end<=R:
        self.update(self._left(p), L, mid, start, end)
        self.update(self._right(p), mid+1, R, start, end)
        p1 = self.st[self._left(p)]
        p2 = self.st[self._right(p)]
        self.st[p] = p1+p2
    
    def rmq(self, start, end):
        return self._rmq(1, 0, self.n-1, start, end)
    
    def _rmq(self, p, L, R, start, end):
        if start>R or end<L:
            return -1
        if L>=start and R<=end:
            return self.st[p]
        mid = (L+R)//2
        p1 = self._rmq(self._left(p), L, mid, start, end )
        p2 = self._rmq(self._right(p), mid+1, R, start, end)
        if p1==-1:
            return p2
        if p2==-1:
            return p1
        # p1 = self.st[self._left(p)]
        # p2 = self.st[self._right(p)]
        return p1+p2
        



        

no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    M = int(input())
    pirates = ""
    for _ in range(M):
        T = int(input())
        pirate = input()
        pirates+=pirate*T
    # print(f"pirate string {pirates}")
    sg = PirateSegmentTree(pirates)
    # print(f"total buca's {sg.st}")
    no_of_op = int(input())
    for _ in range(no_of_op):
        type_of_op, start, end = input().split(" ")
        if type_of_op=='S':
            ans = sg.rmq(int(start), int(end))
            print(f"final ans {ans}")
        else:
            sg.update_val(type_of_op, int(start), int(end))
            # print(f"total buca's post update pirates_list {sg.pirates_list}")
            # print(f"total buca's post update st {sg.st}")
