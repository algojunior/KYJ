import sys
from collections import deque
que = deque()

size = [0,0,0] #h,a,b
size[2], size[1],size[0] = map(int, input().split())
graph =[]
for i in range(size[0]):
    graph.append([])
    for j in range(size[1]):
        arr = [int(x) for x in sys.stdin.readline().split()]
        for k in range(len(arr)):
            if arr[k] == 1:
                que.append((i, j, k))
        graph[i].append(arr)

dx = [0,0,0,0,-1, +1] # 상하좌우전후
dy = [0,0,-1,+1,0,0]
dh =  [-1, +1, 0,0,0,0]

def bfs(graph, size):
    global que
    while len(que):
        nowh, nowa, nowb =  que.popleft()
        for i in range(2,6):
            nexth = nowh + dh[i]
            nexta = nowa + dx[i]
            nextb = nowb + dy[i]

            if 0<=nexth<size[0] and 0<=nexta<size[1] and 0<=nextb<size[2] and graph[nexth][nexta][nextb] == 0:
                que.append((nexth, nexta, nextb))
                graph[nexth][nexta][nextb] = graph[nowh][nowa][nowb] +1

bfs(graph,size)
big = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        for k in range(len(graph[i][j])):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                if graph[i][j][k] > big:
                    big = graph[i][j][k]

print(big-1)






        




