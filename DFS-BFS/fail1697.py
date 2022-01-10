import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

a, b = map(int, input().split())
answer = []
def dfs(v, b, times):
    global answer
    if v > b:
        answer.append(times + (v-b) )
        return
    if v == b:
        answer.append(times)
        return
    dfs(v+1, b, times+1)
    dfs(v-1, b, times+1)
    dfs(2*v, b, times+1)

dfs(a, b, 0)

print(answer.sort())

