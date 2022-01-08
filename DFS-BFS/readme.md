# DFS, 깊이 우선 탐색

## 정의 

Depth-First-Search, 깊이 우선 탐색. 그래프*의 깊은 부분을 우선적으로 탐색하는 알고리즘이다. 

> *그래프: 노드, 간선으로 구성되며, 코딩에서 **인접 행렬** 또는 **인접 리스트**로 표현할 수 있다. 

> 인접 행렬: 메모리 공간이 많이 필요하지만, 접근성이  좋다. 간선이 많을 때 사용
>
> 인접 리스트: 노드 간의 연결 관계를 쉽게 나타날 수 있고, 메모리도 절약할 수 있지만, 접근성이 떨어져서 노드보다 간선이 적을 때 사용

## 특징

1. 스택 구조 사용
2. 코드를 외워서 사용하기

## 과정

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리한다.
2. 스택에 가장 위에 있는 노드의 인접 노드 중에 방문하지 않는 노드가 있다면 해당 노드를 스택에 삽입하고 방문 처리를 한다. 만약 모든 인접 노드가 방문했다면  스택에 가장 위의 노드를 꺼낸다. 
3. 2번 과정을 끝까지 실행한다. 

> 방문처리: 노드의 개수만큼 배열을 따로 만들어서 1,-1/True, False로 해당 노드의 방문상태 표시

## 예시: 이코테 책 예시

### 설명

<img src="https://github.com/algojunior/KYJ/blob/main/DFS-BFS/dfsPhoto.jpg?raw=true" style="zoom:40%;" />

1부터 시작해 깊이 우선 탐색 만듦. 하지만 스택을 대신 **재귀 함수**를 사용해 스택의 효과를 만듦

노드: 숫자로 구성되어 있고, 숫자가 작은 것부터 탐색한다. 

graph: 그래프 데이터, 2차원 (조금 쉬운)인접 리스트로 구성됨.

v: 노드 이름(여기서는 숫자)

visited: 배열, 방문 완료를 표시함. 인덱스가 노드 이름임.

### 코드

```python
def dfs(graph, v, visited):
    visited[v] = True # 방문 처리 하고
    print(v, end=" ") # 출력
    for i in graph[v]: # 노드v에 인접한 노드 중의
        if not visited[i]: # 노드i가 아직 방문 전이라면
            dfs(graph, i, visited) # 재귀적으로 시작.
            
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],    
]

visited = [False] * 9

dfs(graph, 1, visited)
```



# BFS, 너비 우선 탐색

## 정의 

가까운 노드부터 탐색하는 알고리즘. 큐 자료구조를 통해 구현 가능.(인접한 노드를 큐에 놓으면 인접한 노드가 먼저 방문하게 된다.) 나머지는 DFS와 같다. 

## 과정

1. 탐색 시작 노드를 큐에 추가하고 방문 처리를 한다
2. 큐에서 노드를 꺼내 이 노드의 인접한 노드 중에 아직 방문하지 않는 노드 전체 큐에 추가하고 방문 처리한다. 
3. 2번의 과정을 끝까지 한다. 

## 예시

조건은 DFS와 같다.

<img src="https://github.com/algojunior/KYJ/blob/main/DFS-BFS/dfsPhoto.jpg?raw=true" style="zoom:50%;" />

### 코드

```python
from collections import deque 

def bfs(graph, start, visited):
    queue = deque([start]) # 큐 생성(시작 노드 추가하면서)
    visited[start] = True # 시작 노드를 방문함으로 설정
    while queue: # 큐가 빌 때 까지
        v = queue.popleft() #큐에 노드를 꺼낸다.
        print(v, end=" ") # 해당 노드를 출력한다
        for i in graph[v]: # 뽑은 노드의 인접 노드 중에 
            if not visited[i] # 아직 방문 안한 노드i를
            	queue.append[i] # 큐에 추가하고
                visited[i] = True # 방문 표시한다. 
graph = [위와 같다]
visited = [False] * 9
bfs(graph, 1, visited)
```

