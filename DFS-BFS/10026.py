from collections import deque

normalGraph = []
normalCount = 0
specialGraph = []
specialCount = 0

graph = []

n = int(input())
for _ in range(n):
    arr = list(input())
    arr2 = arr[:]
    normalGraph.append(arr)
    specialGraph.append(arr2)

for i in range(n):
    for j in range(len(specialGraph[i])):
        if specialGraph[i][j] == "G":
            specialGraph[i][j] = "R"

def bfs(graph, starta, startb,size,nowColor):
    da = [-1,+1,0,0]
    db = [0,0,-1,+1]
    que = deque()
    graph[starta][startb] = 0
    que.append((starta,startb))
    while len(que) != 0:
        nowa, nowb = que.popleft()
        for i in range(4):
            newa, newb = nowa+da[i], nowb+db[i]
            if 0<=newa<size and 0<=newb<size:
                if graph[newa][newb] == nowColor:
                    graph[newa][newb] = 0
                    que.append((newa, newb))

def pixelbfs(graph,normal=True):
    global normalCount, specialCount,n
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0: continue
            else: 
                bfs(graph, i,j,n,graph[i][j])
                if normal:normalCount+=1
                else: specialCount+=1

pixelbfs(normalGraph)
pixelbfs(specialGraph,False)
print(normalCount,end=" ")
print(specialCount)






