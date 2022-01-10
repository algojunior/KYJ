import sys
sys.setrecursionlimit(10**6)
from collections import deque
# 갈 수 있는 곳을 반환
def checkLoad(graph, nowHigh, nowa, nowb,asize, bsize):
    global que
    aArr = [-1,+1,0,0] #상하좌우
    bArr = [0,0,-1,+1]
    for i in range(4):
        if 0<= nowa+aArr[i] <asize and 0<= nowb+bArr[i] < bsize:
            if graph[nowa+aArr[i]][nowb+bArr[i]] < nowHigh:
                que.append((nowa+aArr[i],nowb+bArr[i]))

def bfs(graph, startHigh, startA, startB):
    global sizeA, sizeB, endHigh, answer,que
    checkLoad(graph, startHigh, startA, startB, sizeA, sizeB)
    while que:
        if len(que) == 0: break
        a, b = que.popleft()
        if graph[a][b] == endHigh:
            answer+=1
        checkLoad(graph, graph[a][b], a, b, sizeA, sizeB)

sizeA, sizeB = map(int, input().split())
graph = []
for i in range(sizeA):
    graph.append([int(x) for x in sys.stdin.readline().split()])

endHigh = graph[sizeA-1][sizeB-1]
answer = 0
que = deque()
bfs(graph, graph[0][0], 0, 0)

print(answer)