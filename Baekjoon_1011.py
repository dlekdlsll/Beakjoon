import math
T = int(input())
case = []

for i in range(0,T):   
    x, y = map(int,input().split())
    d = round(((y-x)/2)-1,)
    times = 1
    N = 1

    while True:
        N += N
        times += 1
        if N > d:
            break
    jump = times+1
    case.append(jump)

[print(i) for i in case]