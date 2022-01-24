n = int(input())

dplist = [0] * (n+1)

for i in range(2,n+1):
    dplist[i] = dplist[i-1] + 1
    if i%2 == 0 and dplist[i] > dplist[i//2]+1:
        dplist[i] = dplist[i//2] +1
    if i%3 == 0 and dplist[i] > dplist[i//3]+1:
        dplist[i] = dplist[i//3] +1
    
print(dplist[n])