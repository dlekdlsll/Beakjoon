A = int(input())
B = int(input())
C = int(input())
K = str(A*B*C)
K = list(K)
for i in range(0,10):
    print(K.count(str(i)))