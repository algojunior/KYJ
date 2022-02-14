n = int(input())
if n == 1:
    print(0)
    print(1)
    exit()
from collections import deque
def bfs():
    check = [0] * (n+1)
    que = deque()
    que.append((1, [1]))
    while que:
        now, nowArr = que.popleft()
        for i in [now+1, now*2, now*3]:
            if i<=n and check[i] == 0:
                if i == n:
                    return check[now]+1, nowArr
                else:
                    check[i] = check[now]+1
                    que.append((i, nowArr+[i]))

a, b = bfs()
print(a)
print(n, end=" ")
for i in range(len(b)-1, -1, -1):
    print(b[i], end=" ")
