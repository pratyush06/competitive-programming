# fenwick tree is only useful when there is a counting problem like how many zeros are there between index 1 4 etc
#  if this current porblem is sligthly tweaked to give Product(number instrad of sign) from index 1 4 we had to use segment tree for that
# also you have to create 1 fenwick tree to track 1 property 

class IntervalProductFenwickTree:
    def __init__(self, no_of_elements):
        self.size = no_of_elements
        self.ft = [None]*self.size
    
    def LSone(self, x):
        return (x&(-x))
    
    def _rsq(self, a):
        ans = 0
        while a>0:
            if self.ft[a]:
                ans+=self.ft[a]
            a-=self.LSone(a)
        return ans
    def rsq(self, a, b):
        return self._rsq(b) - (self._rsq(a-1) if a != 1 else 0)

    def adjust(self, k,v):
        while k<self.size:
            self.ft[k] = self.ft[k] + v if self.ft[k] is not None else v
            # import pdb;pdb.set_trace()
            k+=self.LSone(k)


no_of_elements, no_of_operations = map(int, input().split(" "))
all_elements = list(map(int, input().split(" ")))
all_elements = [None]+all_elements
# print(f"all elements {all_elements}")
zero_fwt = IntervalProductFenwickTree(len(all_elements))
negative_fwt = IntervalProductFenwickTree(len(all_elements))


for idx, val in enumerate(all_elements):
    if idx==0:
        continue
    else:
        if val==0:
            zero_fwt.adjust(idx, 1)
        elif val<0:
            negative_fwt.adjust(idx, 1)

# print(f"fenwick tree {zero_fwt.ft}")
# print(f"fenwick tree {negative_fwt.ft}")

for _ in range(no_of_operations):
    operation, start, end = input().split(" ")
    if operation=='P':
        # import pdb;pdb.set_trace()
        possible_ans = zero_fwt.rsq(int(start), int(end))
        if possible_ans>0:
            print("ans is 0")
        else:
            possible_ans_2 = negative_fwt.rsq(int(start), int(end))
            if possible_ans_2==0 or possible_ans_2%2==0:
                print("ans is +")
            elif possible_ans_2%2!=0:
                print("and is -")
    else:
        # import pdb;pdb.set_trace()
        if int(end)<0 and all_elements[int(start)]>=0:
            negative_fwt.adjust(int(start), 1)
            if all_elements[int(start)]==0:
                zero_fwt.adjust(int(start), -1)
        elif int(end)==0 and all_elements[int(start)]!=0:
            zero_fwt.adjust(int(start), 1)
            if all_elements[int(start)]<0:
                negative_fwt.adjust(int(start), -1)
        elif int(end)>0 and all_elements[int(start)]==0:
            zero_fwt.adjust(int(start), -1)
        elif int(end)>0 and all_elements[int(start)]<0:
            negative_fwt.adjust(int(start), -1)



