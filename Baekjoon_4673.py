def solution():
    S = [str(x) for x in range(1,10001)]
    X = [x for x in range(1,10002)]
    J = []
    for j in S:
        NS = int(j) + sum([int(i) for i in j])
        J.append(NS)
    answer = list(set(X) - set(J))
    answer.sort()
    [print(k) for k in answer]
solution()