import sys
T = sys.stdin.readline()
T = int(T)

K = []
for i in range(0,T):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    K.append(A+B)
for j in K:
    print(j)