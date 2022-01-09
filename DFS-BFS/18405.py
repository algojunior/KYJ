import queue
que = queue.Queue()

n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append( list( map( int, input().split() ) ) )
s, x, y = map(int, input().split())


# graph = [
#     [1,0,2],
#     [0,0,0],
#     [3,0,0]    
# ]

# 1. 주변의 칸의 상황을 반환하는 함수
def checkAround(graph, a, b, n):
    aArr = [-1, +1, 0, 0]
    bArr = [0, 0, -1, +1]
    okArr = []
    for i in range(4):
        if (0 <= (a + aArr[i]) < n) and (0 <= (b + bArr[i]) < n):
            if graph[a + aArr[i] ][ b + bArr[i]] == 0:
                okArr.append((a + aArr[i],b + bArr[i]))
    return okArr
    
# 2. 배열의 있는 좌표들을 해당 숫자로 바꿈:
def changeNum(graph ,abArr, v):
    global que
    for i in abArr:
        que.put(i)
        graph[i[0]][ i[1]] = v

# 3. 1초에 일어나는 일들
def oneTime(graph, que, size):
    nowLocation = que.get()
    while nowLocation:
        now = graph[ nowLocation[0] ][ nowLocation[1] ]
        locations = checkAround(graph,nowLocation[0], nowLocation[1], size)
        changeNum(graph,locations, now)
        nowLocation = que.get()
    que.put(0)

# 4. 시작할 때 바이러스의 순서대로 큐에 좌표를 추가하기
def makeFirstQue(graph, k, size):
    global que
    for i in range(k):
        for a in range(size):
            for b in range(size):
                if graph[a][b] == i+1:
                    que.put((a,b))
    que.put(0)

# 레이스 스타트
def startGame(graph, k, size, s):
    global que
    makeFirstQue(graph, k, size)
    for i in range(s):
        oneTime(graph,que, size)

startGame(graph, k, n, s)
print(graph[x-1][y-1])
            