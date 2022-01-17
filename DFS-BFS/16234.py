from collections import deque
import sys
input = sys.stdin.readline
n, l, r= map(int,input().split())
graph = []
for _ in range(n):
    arr = list(map(int,input().split()))
    graph.append(arr)

def bfs(graph, starta, startb, size):
    da = [-1,+1,0,0]
    db = [0,0,-1,+1]
    global l, r
    oneTeam = []
    que= deque()
    oneTeam.append((starta,startb,graph[starta][startb]))
    que.append((starta,startb,graph[starta][startb]))
    graph[starta][startb] = 0
    while len(que) != 0:
        nowa, nowb, nowPeople= que.popleft()
        for i in range(4):
            newa = nowa + da[i]
            newb = nowb + db[i]
            if 0<=newa<size and 0<=newb<size:
                if graph[newa][newb] != 0 and l<=abs(nowPeople-graph[newa][newb])<=r:
                    oneTeam.append((newa, newb, graph[newa][newb]))
                    que.append((newa, newb, graph[newa][newb]))
                    graph[newa][newb] = 0
    return oneTeam

def rewrite(graph, teamArr):
    peopleArr = []
    count = len(teamArr)
    if count == 1:
        a1,b1,c1 = teamArr[0]
        graph[a1][b1] = c1
        return True
    for i in range(count):
        peopleArr.append(teamArr[i][2])
    if peopleArr.count(peopleArr[0]) == count:
        return True

    avg = int(sum(peopleArr) / count)
    for i in range(count):
        a, b, c = teamArr[i]
        graph[a][b] = avg
    return False

day = 0
def makeTeam(graph, size):
    global day
    ots = []
    for i in range(size):
        for j in range(size):
            if graph[i][j] != 0:
                ots.append(bfs(graph, i, j,size))
    dontmove = 0
    for i in ots:
        a = rewrite(graph,i)
        if a:
            dontmove+=1
    if dontmove == len(ots):
        print(day)
        exit()
    day+=1

while 1:
    makeTeam(graph,n)