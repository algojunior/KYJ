from queue import PriorityQueue
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [ [] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))

def dij(start):
    q = PriorityQueue()
    q.put((0,start))
    distance[start] = 0
    while not q.empty():
        dist, now = q.get()
        if distance[now] < dist: continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.put((cost, i[0]))

dij(start)
for i in range(1,n+1):
    if i == start:
        print("0")
    elif distance[i] == INF:
        print("INF")
    else:
        print(distance[i])






