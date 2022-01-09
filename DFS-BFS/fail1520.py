import sys
sys.setrecursionlimit(10**6)
# 갈 수 있는 곳을 반환
def checkLoad(graph, nowHigh, nowa, nowb,asize, bsize):
    load = []
    aArr = [-1,+1,0,0] #상하좌우
    bArr = [0,0,-1,+1]
    for i in range(4):
        if 0<= nowa+aArr[i] <asize and 0<= nowb+bArr[i] < bsize:
            if graph[nowa+aArr[i]][nowb+bArr[i]] < nowHigh:
                load.append((nowa+aArr[i],nowb+bArr[i]))
    return load

def dfs(graph, nowHigh, nowA, nowB):
    global sizeA, sizeB, endHigh, answer
    todo = checkLoad(graph, nowHigh, nowA, nowB, sizeA, sizeB)
    for i in todo:
        nextHigh = graph[i[0]][i[1]]
        if nextHigh == endHigh:
            answer+=1
        else: dfs(graph, nextHigh, i[0], i[1])

sizeA, sizeB = map(int, input().split())
graph = []
for i in range(sizeA):
    graph.append([int(x) for x in sys.stdin.readline().split()])

endHigh = graph[sizeA-1][sizeB-1]
answer = 0

dfs(graph, graph[0][0], 0, 0)

print(answer)