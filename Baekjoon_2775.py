T = int(input())
floor0 = [i for i in range(1, 15)]

answer = []
solve = 0
for i in range(0,T):
    k = int(input())
    n = int(input())
    for j in range(1,n+1):
        solve += j
    answer.append(solve)
    solve = 0
[print(a) for a in answer] 