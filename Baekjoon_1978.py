N = int(input())
listinin = [int(x) for x in input().split()]

prime = [False,False] + [True]*(1000-1)
for i in range(2,len(prime)):
    if prime[i] == True:
        for j in range(i*2,len(prime),i):
            prime[j] = False
    
printprime = [i for i in listinin if prime[i]==True]
[print(len(printprime))]