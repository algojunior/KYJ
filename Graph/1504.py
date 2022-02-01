from queue import PriorityQueue
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [ [] for _ in range(n+1) ]
distance = [INF] * (n+1)
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a,c))
v2, v3 = map(int, input().split())


def dij(start, graph, distance):
    q = PriorityQueue()
    distance[start] = 0
    q.put((0, start))
    while not q.empty():
        score, now = q.get()
        if distance[now] < score: continue
        for i in graph[now]:
            cost = score + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.put((cost, i[0]))
    return distance

answer1 = dij(1, graph, distance)
distance = [INF] * (n+1)

answer2 = dij(v2, graph, distance)
distance = [INF] * (n+1)

answer3 = dij(v3, graph, distance)
distance = [INF] * (n+1)

total1 = answer1[v2] + answer2[v3] + answer3[n]
total2 = answer1[v3] + answer3[v2] + answer2[n]
if total1>=INF and total2>=INF:
    print(-1)
else:
    print(min(total1, total2))
