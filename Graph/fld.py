import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [ [INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(i, n+1):
        if i == j:
            graph[i][j] == 0

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1,n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
