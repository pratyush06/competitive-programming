from collections import deque
import heapq

def is_priority_queue(pq, expected_ans):
    if not pq:
        return False
    ans = -heapq.heappop(pq)
    return True if ans==expected_ans else False

def is_stack(sc, expected_ans):
    if not sc:
        return False
    ans = sc.pop()
    return True if ans==expected_ans else False

def is_queue(qu, expected_ans):
    if not qu:
        return False
    ans = qu.popleft()
    return True if ans==expected_ans else False
    


while True:
    priority_queue = []
    is_pq = True
    stack = []
    is_sc=True
    dq = deque()
    is_q=True
    try:
        n = int(input())
    except EOFError:
        break # Exit on EOF
    for _ in range(n):
        a, b = map(int, input().split())
        if a==1:
            heapq.heappush(priority_queue, -b)
            stack.append(b)
            dq.append(b)
        elif a==2:
            if is_pq:
                is_pq=is_priority_queue(priority_queue, b)
            if is_sc:
                is_sc=is_stack(stack, b)
            if is_q:
                is_q=is_queue(dq, b)
    
    if (is_pq, is_sc, is_q).count(True)>1:
        print("not sure")
    elif (is_pq, is_sc, is_q).count(True)==0:
        print("impossible")
    elif is_pq:
        print("priority queue")
    elif is_sc:
        print("stack")
    elif is_q:
        print("queue")

