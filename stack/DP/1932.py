import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    arr = list(map(int, input().split(" ")))
    a.append(arr)

for k in range(1,n):
    for j in range(k+1):
        if j == 0:
            a[k][j] += a[k-1][0]
        elif j == k:
            a[k][j] += a[k-1][j-1]
        else:
            a[k][j] += max(a[k-1][j-1], a[k-1][j])
print(max(a[n-1]))
