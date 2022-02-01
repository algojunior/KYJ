import dis
from queue import PriorityQueue
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [ [] for i in range(n+1) ]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))    
distance = [INF] * (n+1)

def dij(start):
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


gox = [0]    
fromx = []            
for i in range(1,n+1):
    distance = [INF] * (n+1)
    if i == start:
        gox.append(0)
        fromx = dij(i)
    else:
        if dij(i)[start] != INF:
            gox.append(dij(i)[start])
        else: gox.append(0)
#print(gox)
#print(fromx)
answer = []
for i in range(1,n+1):
    answer.append(gox[i] + fromx[i])
print(max(answer))