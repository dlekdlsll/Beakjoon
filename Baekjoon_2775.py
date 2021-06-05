T = int(input())
floor0 = [i for i in range(1, 15)]
times = 0
answer = []
solve = 0
TC = []
for i in range(0,T):
    k = int(input())
    n = int(input())
    for j in range(1,n+1):
        test = 1 + times
        solve += j
        times += j
    answer.append(solve)
    TC.append(test)
    solve = 0

[print(a) for a in answer] 
[print(a) for a in TC] 