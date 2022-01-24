n = int(input())
nodeChild = [ [] for _ in range(n+1) ]
arr = list(map(int,input().split()))
for i in range(n):
    if arr[i] == -1:
        nodeChild[n].append(i)
    nodeChild[arr[i]].append(i)
c = int(input())

def returnAll(graph, node):
    arr = [node]
    if len(graph[node]) != 0:
        for i in graph[node]:
            a = returnAll(graph,i)
            arr.extend(a)
    return arr
clear = returnAll(nodeChild,c)

count = 0
for i in range(n):
    if i not in clear:
        if len(nodeChild[i]) == 0:
            count+=1
        elif len(nodeChild[i]) == 1:
            if nodeChild[i][0] in clear:
                count+=1
print(count)
