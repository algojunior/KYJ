from queue import PriorityQueue
import sys
input = sys.stdin.readline
INF = int(1e9)

def dij(start, distance, graph):
    q = PriorityQueue()
    distance[start] = 0
    q.put((0, start))
    while not q.empty():
        score, now = q.get()
        if distance[now] < score: continue
        for i in graph[now]:
            cost = i[1] + score
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.put((cost, i[0]))
    return distance

def makeAnswer(answerList):
    totalCom = 0
    maxTime = 0
    for i in range(1, len(answerList)):
        if answerList[i] != INF:
            totalCom+=1
            if answerList[i] > maxTime:
                maxTime = answerList[i]
    print(totalCom, maxTime)


z = int(input())
for x in range(z):
    n, m, start = map(int, input().split())
    graph = [ [] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for i in range(m):
        a,b,s = map(int, input().split())
        graph[b].append((a, s))
    answer = dij(start, distance, graph)
    makeAnswer(answer)

