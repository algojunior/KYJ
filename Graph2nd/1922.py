from queue import PriorityQueue
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
edge = PriorityQueue()
for i in range(n):
    a,b,c = map(int, input().split())
    edge.put((c,a,b))

family = []
for i in range(n+1):
    family.append(i)

