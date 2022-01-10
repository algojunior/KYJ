import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
    arr = list(input())
    graph.append(arr)

small = 1000000
def bfs(graph):
    global n, m, small
    que = deque()
    graph[0][0] = 1
    que.append((0,0)) #(a, b, 칸수)
    da = [-1, +1, 0, 0]
    db = [0, 0, -1, +1]
    while len(que) != 0:
        nowa, nowb = que.popleft()
        if graph[n-1][m-1] != "1":
            return graph[n-1][m-1]
        else:
            for i in range(4):
                nexta = nowa + da[i]
                nextb = nowb + db[i]
                if 0<=nexta<n and 0<=nextb<m:
                    if graph[nexta][nextb] == '1':
                        graph[nexta][nextb] = graph[nowa][nowb] + 1
                        que.append((nexta, nextb))
                    elif graph[nexta][nextb] != '0':
                        if (graph[nowa][nowb] + 1) < (graph[nexta][nextb]):
                            graph[nexta][nextb] = graph[nowa][nowb] + 1
                            que.append((nexta, nextb))

print(bfs(graph))
