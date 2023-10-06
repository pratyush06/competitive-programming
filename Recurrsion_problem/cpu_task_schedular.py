from typing import List


def cpuTaskScheduler(n: int, arr: List[List[int]]):
    no_of_cores={}
    for i, j in arr:
        check_free_core(no_of_cores, i, j)
    
    print(no_of_cores)


def check_free_core(no_of_cores, curr_start_time, end_time):
    status=False
    core=0
    for i, j in no_of_cores.items():
        core+=1
        if j<=curr_start_time:
            status=True
            no_of_cores[i]=end_time
            break
    core+=1
    if not status:
        no_of_cores[core]=end_time
    return status
        
    
def modifiedcpuTaskScheduler(n, arr):
    core=[]
    arr.sort()
    for i, j in arr:
        core.sort()
        if len(core)==0:
            core.append(j)
        elif core[0]<=i:
            core[0]=j
        else:
            core.append(j)
    print(core)





n=4
arr=[[0,10], [10, 25], [5,20], [30, 40]]

s=modifiedcpuTaskScheduler(n, arr)