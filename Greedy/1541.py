# 입력: a=괄요 없는 수식
a = input()

# 플이: 이 문제의 핵심은:
# "더할 수 있는 모든 값을 더하고 마이너스'-' 로 빼자"
# 이다. 숫자의 위치는 변할 수 없기에 다른 예외 상황도 없다.

tmp = a.split("-") 
# 먼저 마이너스로 뺄 수 있는 덩어리를 나눠본다.

def addFunc(str):# '+'가 포함한 덩어리의 결과값을 계산하는 함수
    addNum = list(map(int,str.split("+")))
    # '+'로 숫자들을 나누고 합을 구하면 끝
    return sum(addNum)

# '+'를 포함한 여러 숫자/'+'수식 덩어리를 순환
for i in range(len(tmp)):
    if "+" in tmp[i]: tmp[i] = addFunc(tmp[i])
    # 수식이면 숫자로 바꾸기
    else: tmp[i] = int(tmp[i])
    # 안 그러면 그냥 int형으로만 바꾸면 됨.

hap = sum(tmp[1:])
# 편의상 두 번째 숫자부터 마지막 숫자까지 하나의 큰 괄호로 묶고
print(tmp[0] - hap)

# 예시: 
# 50+20-30-40+20 -> (50+20) - (30+(40+20))
    