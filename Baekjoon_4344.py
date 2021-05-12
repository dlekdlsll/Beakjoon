C = int(input())
k = 0
s = []
for c in range(0,C):
    R = list(map(int,input().split()))
    P = R[0]
    for p in range(0,P):
        k = 0
        for r in range(1,len(R)):
            if sum(R)/P <= R[r] :
                k += 1
    s.append((k/P)*100)
for i in s:
    print(format(round(i,3),"0.3f"))