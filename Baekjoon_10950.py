T = input()
T = int(T)
A = []
for i in range(T):
    k,c = input().split()
    k = int(k)
    c = int(c)
    A.append(k+c)
for j in range(T):
    print(A[j])