#입력: n=동전 종류 개수, k=만들 금액
n, k = map(int,input().split(" "))
coinList = [] # 각 종류의 동전 금액
for i in range(n):
    coinList.append(int(input()))

#모든 동전이 배수이기 때문에
#그냥 액수가 큰 동전부터 금액을 만들면 끝
answer = 0
for i in range(len(coinList)-1,-1,-1):
    answer += k//coinList[i]
    k = k%coinList[i]
    if k == 0: break
print(answer)