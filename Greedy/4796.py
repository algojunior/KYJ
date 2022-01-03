# 문제만 이해한다면 어렵지 않아유
# 연속된 20(P)일 동안 10(L)일만 사용 가능하는 호텔이 있다.
# 나는 28(V)일의 휴가가 있으면 이 호텔에서 최대 얼마 살 수 있을까?
# 즉: 28(V)일의 휴가 중: 첫 20(P)일은 10(L)일동안 사용하고, 
# 나머지 8일은 다음의 20(P)일 중의 8일만 즐기고 가면 되니까
# 총 18일동안 이 호텔에 살 수 있는 거지

i=0
# 이거는 여러 번 실행하기 때문에
while 1: 
    i+=1# 출력 횟수를 위한 변수임
    l,p,v=map(int,input().split(" "))
    if l+p+v==0:break # 모두 0이면 실행 종료
    else:
        a = v%p # 일단 전체 후일 중 몇 개의 P가 있는지
        if a>l: a = l # 만약 남은 휴일이 L보다 많아도 L일만 사용 가능
        print("Case",str(i)+":",(v//p)*l+a) 