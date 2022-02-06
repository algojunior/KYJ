from queue import PriorityQueue
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [ [] for i in range(n+1)]
visited = [False] * (n+1)
lock = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    lock[b]+=1

def order(lock):
    todo = PriorityQueue()
    for i in range(1,n+1):
        if lock[i] == 0: todo.put(i)

    while not todo.empty():
        now = todo.get()
        for i in graph[now]:
            lock[i] -=1
            if lock[i] == 0: todo.put(i)
        print(now, end=" ")

order(lock)
