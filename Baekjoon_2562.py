A = []
for i in range(0,9):
    j = int(input())
    A.append(j)
A = list(A)
print(max(A))
print(A.index(max(A))+1)