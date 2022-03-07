import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

qstack = [0, 1]
answer = ["+"]
now = 1
for i in range(n):
    if a[i] == qstack[-1]:
        qstack.pop()
        answer.append("-")
        continue
    elif a[i] < qstack[-1]:
        print("NO")
        exit()
    while qstack[-1] < a[i]:
        now +=1
        qstack.append(now)
        answer.append("+")
    qstack.pop()
    answer.append("-")
for i in answer: print(i)

