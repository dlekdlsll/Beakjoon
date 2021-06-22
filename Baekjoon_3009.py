answer = []

for i in range(0,3):
    A, B = map(int,input().split())
    answer.append(A); answer.append(B)

for i in answer: 
    if answer.count(i)==2: k = i

print(k,k)