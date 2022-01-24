n = int(input())
dp = [[0,0] for _ in range(n+1)]
#[0,0]에서 앞은 한 번에 두개씩 올라오는 경우 중에 가장 큰 점수
#          뒤는 한 번에 한 계단을 올라올 때 가장 큰 점수

score = [0]
for i in range(n):
    score.append(int(input()))

dp[1][0] = score[1]
for i in range(2, n+1):
    # 두 계단씩 올라오는 방법 중에 가장 높은 점수
    dp[i][0] = score[i] + max(dp[i-2][0], dp[i-2][1])
    # 바로 이전의 계단에서 올라올 때의 점수
    dp[i][1] = score[i] + dp[i-1][0]

print(max(dp[n][0], dp[n][1])) 
