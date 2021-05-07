T = input()
T = int(T)
K = []
S = []
t = 1

for i in range(0,T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    K.append(A+B)
    S.append('{} + {}'.format(A,B))
for j in (K):
    print('Case #{}: {} = {}'.format(t,S[t-1],j))
    t += 1