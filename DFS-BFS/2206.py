from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input()[0:-1])))

def tpList2str(list):
    ans = ""
    for i in list:
        a,b = i
        ans+=str(a)
        ans+=str(b)
    return ans

def str2tpList(st):
    lst = []
    for i in range(0,len(st)-1,2):
        lst.append((int(st[i]),int(st[i+1])))
    return lst

def bfs(graph):
    da = [1,0,0,-1] #하 우 좌 상
    db = [0,+1,-1,0]
    global n, m
    answer  = 100000000
    answerArr = []
    que = set() #set:[x,y,부수기,[튜플로 걸어왔던 길을 표시]]
    que.add((0,0,False,"00"))
    while que:
        nowa, nowb, ToF, nowLoadStr = que.pop()
        nowLoad = str2tpList(nowLoadStr)
        if nowa == n-1 and nowb == m-1:
            answerArr.append(len(nowLoad))
        for i in range(4):
            newa, newb = nowa+da[i], nowb+db[i]
            if 0<=newa<n and 0<=newb<m and (newa,newb) not in nowLoad:
                if graph[newa][newb] == 0:
                    tmp = nowLoad[:]
                    tmp.append((newa,newb))
                    que.add((newa,newb,ToF,tpList2str(tmp)))
                    answer = min(answer,len(nowLoad)+1)
                else:
                    if not ToF:
                        tmp = nowLoad[:]
                        tmp.append((newa,newb))
                        que.add((newa,newb,True,tpList2str(tmp)))
                        answer = min(answer,len(nowLoad)+1)
    return answerArr
end = bfs(graph)
if len(end) == 0:
    print(-1)
else:
    end.sort()
    print(end[0])




