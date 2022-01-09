from collections import deque
import sys

#해결 방법:
# 대부분 방법은 visited배열을 distance배열으로 
# 사용해 현재의 최단 거리를 저장(다익스트라도 생각이 나고)
#
#
#
#
#
#
#
#
#
#
#

#입력 단계
n, m, k, x = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    s, e = [int(x) for x in sys.stdin.readline().split()]
    graph[s].append(e)

#bfs함수
def bfs(graph, start, visited,needDis):
    queue = deque([start,-1])
    visited[start] = True
    distance = 1
    answer = []
    while queue:
        v = queue.popleft()

        if v == -1: # 
            if distance == needDis:
                while queue:
                    answer.append(queue.popleft())
                return answer
            else: 
                distance+=1
                queue.append(-1)
                continue

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return queue

answer = bfs(graph,x, visited,k)

if len(answer) == 0: 
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
