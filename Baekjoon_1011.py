case = []

for i in range(0,int(input())):   
    x, y = map(int,input().split())
    d = y-x; times = 1; jump = 0; N = 1    
    
    while True:
        N += times
        jump += 1
        if jump % 2 == 0: times += 1
        if N > d: break
    case.append(jump)

[print(i) for i in case]