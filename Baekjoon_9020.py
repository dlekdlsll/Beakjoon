sosu = []
odd = [1,3,5,7,9]
for T in range(0,int(input())):
    n = int(input())
    while True:
        n = n//2
        for i in odd:
            if (n+i)