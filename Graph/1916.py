from queue import PriorityQueue
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())
distance = [INF] * (n+1)

def dit(start):
    q = PriorityQueue()
    q.put((0, start))
    distance[start] = 0 # 중요
    while not q.empty():
        score, now = q.get()
        if distance[now] < score: continue # 중요
        for i in graph[now]:
            if distance[now] + i[1] < distance[i[0]]:
                distance[i[0]] = distance[now] + i[1]
                q.put((distance[i[0]], i[0])) # 중요

dit(start)

print(distance[end])
