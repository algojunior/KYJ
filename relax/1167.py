import sys
INF = int(1e9)
input = sys.stdin.readline

n = int(input())
graph = [ [] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(n):
    arrList = list(map(int, input().split()))
    first = arrList[0]
    for j in range(1,len(arrList)-1,2):
        graph[first].append((arrList[j], arrList[j+1]))

def dfs(start, visited):
    for node, value in graph[start]:
        if visited[node] == 0:
            visited[node] = visited[start] + value
            dfs(node, visited)

dfs(1,visited)
visited[1] = 0
maxValue = 0
maxIdx = 0
for i in range(n+1):
    if visited[i] > maxValue:
        maxValue = visited[i]
        maxIdx = i
visited = [0] * (n+1)
dfs(maxIdx, visited)
visited[maxIdx] = 0
print(max(visited))


