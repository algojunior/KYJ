from queue import PriorityQueue
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n+1)
graph = [ PriorityQueue() for i in range(n+1) ]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].put(a)

def heightDfs(now):
    if visited[now]: return 0
    while not graph[now].empty():
        new = graph[now].get()
        heightDfs(new)
    visited[now] = True
    print(now, end=" ")

for i in range(1,n+1):
    heightDfs(i)