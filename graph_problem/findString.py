#Topological sorting
import queue
def findWord(li):
    graph={}
    indegree={}
    for i in li:
        graph[i[0]]=[]
        graph[i[2]]=[]
        indegree[i[0]]=0
        indegree[i[2]]=0
    for i in li:
        indegree[i[2]]+=1    
        graph[i[0]].append(i[2])
    L=queue.Queue()
    L.put(list(indegree.keys())[list(indegree.values()).index(0)])
    
    ans=""
    while not L.empty():
        # import pdb;pdb.set_trace()
        # print(L.get())
        element=L.get()
        # element=next(ele)
        ans+=element
        # print(element)
        for i in graph[element]:
            indegree[i]-=1
            if indegree[i]==0:
                L.put(i)
        element=None
    print(ans)
    
    
    

    
    # pass

findWord(["P>E","E>R","R>U"])
findWord(["I>N","A>I","P>A","S>P"])
findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"])
findWord(["I>F", "W>I", "S>W", "F>T"])
findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"])
findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"])