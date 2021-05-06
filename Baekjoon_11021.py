T = input()
T = int(T)
K = []
t = 1

for i in range(0,T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    K.append(A+B)
for j in (K):
    print('Case #{}: {}'.format(t,j))
    t += 1