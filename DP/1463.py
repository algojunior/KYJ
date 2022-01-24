t = int(input())
tlist = []
for i in range(t):
    tlist.append(int(input()))

dplist = [0] * (max(tlist)+1)
zeroList = [0] * (max(tlist)+1)
oneList = [0] * (max(tlist)+1)

dplist[0] = 0
dplist[1] = 1
zeroList[0] = 1
oneList[1] = 1
for i in range(2,max(tlist)+1):
    dplist[i] = dplist[i-1] + dplist[i-2]
    zeroList[i] = zeroList[i-1] + zeroList[i-2]
    oneList[i] = oneList[i-1] + oneList[i-2]

for j in tlist:
    print(zeroList[j],end=' ')
    print(oneList[j])
