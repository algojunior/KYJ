import queue,sys
que = queue.Queue()
leftTomato = 0

def choose(graph, a, b, h, size):
    global que,leftTomato
    xArr = [0,0,0,0,-1, +1] # 상하좌우전후
    yArr = [0,0,-1,+1,0,0]
    hArr = [-1, +1, 0,0,0,0]
    for i in range(6):
        if 0<=h+hArr[i]<size[0] and 0<=a+xArr[i]<size[1] and 0<=b+yArr[i]<size[2]:
            if graph[h+hArr[i] ][ a+xArr[i] ][ b+yArr[i]] == 0:
                graph[h+hArr[i]][a+xArr[i]][b+yArr[i]] = 1
                leftTomato -=1
                que.put((h+hArr[i],a+xArr[i],b+yArr[i]))

def bfs(graph,size):
    global que,leftTomato
    day = 0
    while que:
        day+=1
        if leftTomato == 0:
            return day
        now = que.get()
        while now:
            choose(graph, now[1], now[2], now[0],size)
            if leftTomato == 0:
                return day
            now = que.get()
        if que.empty():
            return -1
        else: que.put(0)
    return -1

size = [0,0,0] #h,a,b
size[2], size[1], size[0] = map(int, input().split())

graph =[]
for i in range(size[0]):
    graph.append([])
    for j in range(size[1]):
        arr = [int(x) for x in sys.stdin.readline().split()]
        #leftTomato+=arr.count(0)
        for k in range(len(arr)):
            if arr[k] == 0:
                leftTomato +=1
            elif arr[k] == 1:
                que.put((i, j, k))
        graph[i].append(arr)
que.put(0)
if leftTomato == 0:
    print(0)
else:
    print(bfs(graph, size))






        




