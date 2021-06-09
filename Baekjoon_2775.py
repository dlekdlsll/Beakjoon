T = int(input())
answer = []

for i in range(0,T):
    floor = [i for i in range(1, 15)]
    k = int(input())
    n = int(input())
    for j in range(0,k):
        for k in range(1,n):
            floor[k] = floor[k]+floor[k-1]
    answer.append(floor[n-1])

[print(a) for a in answer] 