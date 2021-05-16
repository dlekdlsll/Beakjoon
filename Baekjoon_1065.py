def solution():
    N = int(input())
    X = [str(x) for x in range(1,N+1)]
    i = 0

    for x in X:
        if len(x)<2:
            i += 1
        else:
            Solve = {int(x[-s]) - int(x[-s-1]) for s in range(1,len(x))}
            if len(Solve) == 1:
                i += 1
    return(i)
print(solution())