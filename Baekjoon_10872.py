N = int(input())
if N == 1: print(1)
if N == 0: print(0)
if N != 1 and N != 0:
    for i in range(N-1,1,-1):
        N = N*i
    print(N)