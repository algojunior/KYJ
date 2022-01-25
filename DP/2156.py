n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dp1 = [0] * n
dp2 = [0] * n
dp1[0] = arr[0]

for i in range(1,n):
    for j in range(1,i):
        dp1[i] = max(dp1[i])
    

