N, M = map(int,input().split())
listinin = [int(x) for x in range(N,M+1)]

prime = [False,False] + [True]*(1000000-1)
for i in range(2,len(prime)):
    if prime[i] == True:
        for j in range(i*2,len(prime),i):
            prime[j] = False
    
printprime = [i for i in listinin if prime[i]==True]

[print(x) for x in printprime]