while True:
    k = input()
    if not k:
        break
    else:
        k=int(k)
    x=k+1
    print(f"x: {x}")
    ans = set()
    while True:
        print(f"indside{x}")
        ans_1=(x-k)/(k*x)
        # import pdb;pdb.set_trace()
        ans_2 = (1/k)-ans_1
        if (k*x)%(x-k)==0:
            ans.add((ans_1, ans_2))
        if ans_2==ans_1:
            break
        else:
            x+=1
        # if x==6:
        #     break
    
    print(ans)
    print(len(ans))