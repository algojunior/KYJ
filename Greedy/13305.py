#입력: n=도시의 개수 load=각 길의 오일 사용량 oil=각 도시의 오일 가격
n = int(input())
load = list(map(int, input().split(" ")))
oil = list(map(int, input().split(" ")))

# 아이디어: 가장 기본적인 생각은: 가장 낮은 곳에서 기름을 많이 놓어야
# 만약 출발 도시의 기름이 가장 싸다: 출발 도시에서 기름 잔뜩 놓고 출발하면 되지
# 하지만 그런 상황이 별로 없죠...그렇다고 해서 출발 안하면 또 안 되고
# 어쨌든 일단 출발을 해야 되니까 출발도시에서 기름을 놓어야 되는데
# 출발 도시에서 기름을 끝까지 놓으면 
# 나중에 "지금보다 더 싼 곳"이 있으면 완전 손해
# 그래서 출발 도시에서 기름을 얼마나 놓어야 가장 경제적일까:
'''
# "지금보다 더 싼 가격인 도시"까지만 갈 수 있는 기름 양을 놓으면
# 더 싼 가격인 도시에 도착하자마자 거기의 기름을 놓는게 가장 좋겠죠?
'''
# 그럼 그 다음은 어떻게야 돼? -> 위 방법을 반복 사용하면 되지!

answer = 0 # 최종 비용
nowIdx = 0 # 현재 위치
while 1:
    endgame = False 
    # 기름의 가격이 1원인 도시를 만나면 거기서 기름 잔뜩 놓으면 되니까 이 때는 True로 바꾸자
    nowOilMoney = oil[nowIdx] # 현재 도시의 기름값
    needOil = 0 # 기름이 지금보다 싼 곳에 도착하기 위해 필요한 기름의 양

    # 현재 도시의 다음도시부터 마지막 도시까지
    for i in range(nowIdx+1,len(oil)):
        needOil += load[i-1] 
        # 한 도시에 지나갈 때마다 필요한 기름을 계산하고

        if i == len(oil) - 1: # '기름이 현재 도시보다 싼 도시'가 없다면
            answer += nowOilMoney * needOil # 최종 금액을 추가하고
            nowIdx = i # 현재 도시를 마지막 도시로 설정
            break

        if oil[i] == 1: # 기름값이 1원인 도시 발견 시
            answer += nowOilMoney * needOil # 기름 마지막 도시까지 갈 양을 채워!
            nowIdx = i # 마지막 도시까지 감
            endgame = True #Game Over
            break

        if oil[i] < nowOilMoney: # 현재 도시보다 기름이 싼 도시를 찾았다!!!
            answer += nowOilMoney * needOil # 해당 도시까지의 기름값만 계산하고
            nowIdx = i #해당 도시까지 간다.
            break

    if endgame: #1원인 곳이 있다면
        answer += sum(load[nowIdx:]) # 나머지 도로의 길에 필요한 기름 == 기름값
        break
    if nowIdx == len(oil) - 1: break # 마지막 도시까지 갔다면 종료
print(answer)


        


