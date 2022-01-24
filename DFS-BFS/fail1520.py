import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
# 갈 수 있는 곳을 반환

n, m = map(int,input().split())
graph = []
dp = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    dp.append([-1] * (m))

def dfs(graph,a,b):
    global n, m, dp
    if a == n-1 and b == m-1:
        return 1
    if dp[a][b] == -1:
        dp[a][b] = 0
        for da, db in [(-1,0), (1,0), (0,-1), (0,1)]:
            newa,newb = a+da,b+db
            if 0<=newa<n and 0<=newb<m:
                if graph[a][b]>graph[newa][newb]:
                    dp[a][b] += dfs(graph, newa, newb)
    return dp[a][b]

print(dfs(graph,0,0))


