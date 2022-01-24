import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
graph = [ [] for _ in range(v+1) ]
bigOne = 0
bigPrice = 0
for i in range(v):
    arr = list(map(int,input().split()))
    for j in range(1,len(arr)-2,2):
        if arr[j+1] > bigPrice:
            bigOne = arr[j]
            bigPrice = arr[j+1]
        graph[arr[0]].append((arr[j], arr[j+1]))


def bfs(graph, start,size):
    biggest = 0
    estHistory = []
    bigger = 0
    erHistory = []
    visited = [False] * (size+1)
    que = deque()
    que.append((start,0,[]))
    visited[start] = True
    while len(que) != 0:
        now,nowPrice, nowhistory= que.popleft()

        if len(graph[now]) == 1 and now != start:
            if nowPrice > biggest:
                if len(set(estHistory) & set(nowhistory)) == 0:
                    bigger = biggest
                    erHistory = estHistory
                    biggest = nowPrice
                    estHistory = nowhistory
                else:
                    biggest = nowPrice
                    estHistory = nowhistory
            elif nowPrice > bigger:
                if len(set(estHistory) & set(nowhistory)) == 0:
                    bigger = nowPrice
                    erHistory = nowhistory
        for i in graph[now]:
            new, newPrice = i
            if not visited[new]:
                visited[new] = True
                newHistory = nowhistory[:]
                newHistory.append(new)
                que.append((new, newPrice + nowPrice,newHistory))
    return biggest + bigger

print(bfs(graph,bigOne,v))
