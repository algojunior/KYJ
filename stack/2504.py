a = input()
qstack = []
if a[0] in ["]", ")"]:
    print(0)
    exit()
for i in a:
    if i in ["[", "("]:
        qstack.append(i)
    elif i == "]" and len(qstack) >0:
        last = qstack.pop()
        if last == "[":
            qstack.append(3)
        elif isinstance(last, int):
            number = last
            while 1:
                if len(qstack) == 0:
                    print(0)
                    exit()
                last = qstack.pop()
                if last == "[":
                    qstack.append(number * 3)
                    break
                elif isinstance(last, int):
                    number +=last
                    continue
                else:
                    print("0")
                    exit()
        else:
            print(0)
            exit()
    elif i == ")" and len(qstack) >0:
        last = qstack.pop()
        if last == "(":
            qstack.append(2)
        elif isinstance(last, int):
            number = last
            while 1:
                if len(qstack) == 0:
                    print(0)
                    exit()
                last = qstack.pop()
                if last == "(":
                    qstack.append(number * 2)
                    break
                elif isinstance(last, int):
                    number +=last
                    continue
                else:
                    print("0")
                    exit()
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()
answer = 0
for i in qstack:
    if isinstance(i, int):
        answer+=i
    else:
        print(0)
        exit()
print(answer)

