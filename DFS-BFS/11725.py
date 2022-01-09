import sys
sys.setrecursionlimit(10**6)
# 노드 클래스 만듦
class node:
    dad = 0

    def __init__(self):
        self.dad = 0

    def setDad(self, dadNum):
        self.dad = dadNum
    
    def getDad(self):
        return self.dad

n = int(input())

nodeArr = []
nodeArr.append(node())
graph = [ [] ]
visited = [False] * (n+1)
for i in range(n):
    nodeArr.append(node())
    graph.append([])

for i in range(n-1):
    a,b = [int(x) for x in sys.stdin.readline().split()]
    # 여기서 graph 변수는 쌍방향으로 만듦(1,6이면 graph[1]에 6을, [6]에 1를 두 번 추가하기)
    graph[a].append(b)
    graph[b].append(a)

# 1부터 방문해 
visited[1] = True
def dfs(graph, nodeArr, v, visited):
    for i in graph[v]:
        if visited[i]:# 이미 방문한 값 -> 위에서 넘어온 부모값이니까 부모값 설정
            nodeArr[v].setDad(i)
        else:  # 아직 방문 하지 않는 노드는 자식이다. 
            visited[i] = True
            dfs(graph, nodeArr, i, visited)

dfs(graph,nodeArr,1,visited)

for i in range(2,len(nodeArr)):
    print(nodeArr[i].getDad())
