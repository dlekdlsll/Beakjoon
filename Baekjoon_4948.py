answer = []
while True :
  N = int(input())
  if N==1:
    answer.append(1)
    continue
  if N==0:
    [print(x) for x in answer]
    break
  listinin = [int(x) for x in range(N+1,N*2)]

  prime = [False,False] + [True]*(N*2)
  for i in range(2,len(prime)):
      if prime[i] == True:
          for j in range(i*2,len(prime),i):
             prime[j] = False
    
  printprime = [i for i in listinin if prime[i]==True]
  answer.append(len(printprime))