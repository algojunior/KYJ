from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int,input().split())
graph = []
for i in range(r):
    graph.append(list(input())[0:-1])

def bfs(graph):
    global r,c
    answer = 1
    da = [-1,+1,0,0]
    db = [0,0,-1,+1]
    que = set([(0,0,graph[0][0])])
    while len(que) != 0:
        nowa, nowb, nowLoad = que.pop()
        for i in range(4):
            newa, newb = nowa+da[i], nowb + db[i]
            if(0<=newa<r)and(0<=newb<c)and graph[newa][newb] not in nowLoad:
                que.add((newa, newb, nowLoad+graph[newa][newb]))
                answer = max(answer, len(nowLoad)+1)
    return answer
print(bfs(graph))

