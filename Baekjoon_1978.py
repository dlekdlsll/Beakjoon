N = int(input())
listinin = [int(x) for x in input().split()]; sosu = []
for i in range(0,N): 
    A = listinin[i]
    if A!=1:
        if A==2 | A%2!=0: sosu.append(A) 
        elif A==3 | A%3!=0: sosu.append(A) 
        elif A==5 | A%5!=0: sosu.append(A) 
        elif A==7 | A%7!=0: sosu.append(A)
        elif A==11 | A%11!=0: sosu.append(A)
print(len(sosu))