N = int(input())
S = N
i = 0
while N < 100:
    A = N//10
    B = N % 10
    K = (B*10)+((A+B)%10)
    N = K
    i += 1
    if N == S :
        print(i)
        break