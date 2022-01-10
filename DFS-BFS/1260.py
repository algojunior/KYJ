from collections import deque
import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())
mainGraph = [ [] for _ in range(n+1) ]

for i in range(m):
    a,b = map(int, input().split())
    mainGraph[a].append(b)
    mainGraph[b].append(a)

for i in mainGraph:
    i.sort()
dfsVisited = [False] * (n+1)
dfsVisited[v] = True
def dfs(graph, v, visited):
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)
dfs(mainGraph, v, dfsVisited)
print()

bfsVisited = [False] * (n+1)
def bfs(graph, start, visited):
    print(start, end=" ")
    visited[start] = True
    que = deque()
    que.append(start)
    while len(que) != 0:
        now = que.popleft()
        for i in graph[now]:
            if not visited[i]:
                print(i, end=" ")
                visited[i] = True
                que.append(i)
bfs(mainGraph, v, bfsVisited)


        

