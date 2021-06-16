N = int(input()); M = int(input())
listinin = [int(x) for x in range(N,M+1)]

prime = [False,False] + [True]*(10000-1)
for i in range(2,len(prime)):
    if prime[i] == True:
        for j in range(i*2,len(prime),i):
            prime[j] = False
    
printprime = [i for i in listinin if prime[i]==True]

if len(printprime) > 1: print(sum(printprime)); print(min(printprime))
elif len(printprime) == 1: print(printprime[0]); print(printprime[0])
else: print(-1)