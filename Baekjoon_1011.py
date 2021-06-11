T = int(input())
case = []

for i in range(0,T):   
    x, y = map(int,input().split())
    d = y-x-1
    distance = [-1,0,1]
    times = 1
    jump = 1

    while True:
        if d == 0:
            break
        d -= jump
        distance = [jump-1,jump,jump+1]
        if d in distance and max(distance) <= 3 and d > 0 and d!=3 :
            times += 1
            d -= d
        jump = max(distance)
    case.append(times)
    
[print(i) for i in case]