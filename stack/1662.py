a = input()
qstack = []
answer = 0
for i in a:
    if i in ["0", '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']:
        qstack.append(i)
        continue
    elif i == ")":
        intStr = ""
        num = 0
        while 1:
            last = qstack.pop()
            if last in ["0", '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                intStr += str(last)
                continue
            elif last == "(":
                strlen = len(intStr) + num
                kupnum = int(qstack.pop())
                qstack.append(kupnum * strlen)
                break
            elif isinstance(last, int):
                num += last
                continue

for k in qstack:
    if isinstance(k, str):
        answer +=1
    else:
        answer+=k
print(answer)


