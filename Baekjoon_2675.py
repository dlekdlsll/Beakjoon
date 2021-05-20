T = int(input())
result = []

for t in range(0,T):
    S1 = input().split()
    R = int(S1[0])
    S2 = list(S1[1])
    P = ''
    
    for s in S2:
        word = s*R
        P = P + word
    result.append(P)
for x in result:print(x)