n = int(input())
numArr = list(map(int, input().split()))
calcNumArr = list(map(int, input().split()))
calcArr = []
calc = ['+', '-', '*', '/']
for i in range(len(calc)):
    for j in range(calcNumArr[i]):  
        calcArr.append(calc[i])

from itertools import permutations
all = list(permutations(calcArr))

def calcNum(numArr, Arr):
    end = numArr[0]
    for i in range(1, len(numArr)):
        b = numArr[i]
        if Arr[i-1] == '+':
            end = end + b
        elif Arr[i-1] == '-':
            end = end - b
        elif Arr[i-1] == '*':
            end = end*b
        elif Arr[i-1] == '/':
            if end < 0 and b>0:
                tmp = -(end)
                tmp = tmp // b
                end = -(tmp)
            else:
                end = end//b
    return end

big = calcNum(numArr,all[0])
small = calcNum(numArr,all[0])

for i in all:
    this = calcNum(numArr,i)
    if this > big: 
        big = this
    elif this < small:
        small = this

print(big)
print(small)



