import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

da = [-1, +1, 0, 0]
db = [0, 0, -1, +1]
enda, endb = n-1, m-1
answer = 0
def dfs(graph, nowa, nowb):
    global enda, endb, da, db, answer
    if nowa == enda and nowb == endb:
        answer+=1
    else:
        for i in range(4):
            nexta = nowa + da[i]
            nextb = nowb + db[i]
            if 0<=nexta<=enda and 0<=nextb<=endb:
                    if graph[nexta][nextb] < graph[nowa][nowb]:
                        dfs(graph, nexta, nextb)

dfs(graph, 0, 0)
print(answer)


