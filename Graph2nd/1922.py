from queue import PriorityQueue
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
edge = PriorityQueue()
for i in range(m):
    a,b,c = map(int, input().split())
    edge.put((c,a,b))

parent = []
for i in range(n+1):
    parent.append(i)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def unionNode(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
while True:
    if sum(parent) == n:
        print(answer)
        exit()
    nowScore, nowa, nowb = edge.get()
    if find_parent(parent, nowa) != find_parent(parent, nowb):
        unionNode(parent, nowa, nowb)
        answer+=nowScore

