import math
T = int(input())
case = []

for i in range(0,T):   
    x, y = map(int,input().split())
    d = round((y-x)/2)
    times = 1
    N = 1

    while True:
        if N > d:
            break
        N += N
        times += 1
    jump = (times*2)+1
    case.append(jump)

[print(i) for i in case]