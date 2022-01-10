import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

enda, endb = n-1, m-1
def bfs(graph, enda, endb):
    da = [-1, +1, 0, 0]
    db = [0, 0, -1, +1]
    answer = 0
    que = deque()
    que.append((0, 0))
    while len(que) != 0:
        nowa, nowb = que.popleft()
        if nowa == enda and nowb == endb:
            answer +=1
        else: 
            for i in range(4):
                nexta = nowa + da[i]
                nextb = nowb + db[i]
                if 0<=nexta<=enda and 0<=nextb<=endb:
                    if graph[nexta][nextb] < graph[nowa][nowb]:
                        que.append((nexta,nextb))
    return answer

print(bfs(graph, enda, endb))



