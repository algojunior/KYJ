import queue,sys
que = queue.Queue()

def choose(graph, a, b, h, size):
    global que
    xArr = [0,0,0,0,-1, +1] # 상하좌우전후
    yArr = [0,0,-1,+1,0,0]
    hArr = [-1, +1, 0,0,0,0]
    for i in range(6):
        if 0<=h+hArr[i]<size[0] and 0<=a+xArr[i]<size[1] and 0<=b+yArr[i]<size[2]:
            if graph[h+hArr[i] ][ a+xArr[i] ][ b+yArr[i]] == 0:
                graph[h+hArr[i]][a+xArr[i]][b+yArr[i]] = graph[h][a][b] + 1
                que.put((h+hArr[i],a+xArr[i],b+yArr[i]))

def bfs(graph,size):
    global que
    while que:
        now = que.get()
        while now:
            choose(graph, now[1], now[2], now[0],size)
            now = que.get()
            if que.empty():
                return graph
    return graph

size = [0,0,0] #h,a,b
size[2], size[1] = map(int, input().split())
size[0] = 1
graph =[]
for i in range(size[0]):
    graph.append([])
    for j in range(size[1]):
        arr = [int(x) for x in sys.stdin.readline().split()]
        graph[i].append(arr)

for i in range(len(graph)):
    for j in range(len(graph[i])):
        for k in range(len(graph[i][j])):
            if graph[i][j][k] == 1:
                que.put((i, j, k))
if que.empty():
    print(0)
    exit(0)
graph = bfs(graph,size)
big = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        for k in range(len(graph[i][j])):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            elif graph[i][j][k] >big:
                big = graph[i][j][k]
print(big-1)






        




