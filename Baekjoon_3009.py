X, Y = [],[]
for _ in range(3):    # 인자없이 3번 반복합니다
    x, y = map(int, input().split())
    X.append(x); Y.append(y)
for i in range(3):   # 3번 반복 합니다
    if X.count(X[i]) == 1: x2 = X[i]
    if Y.count(Y[i]) == 1: y2 = Y[i]
print(x2, y2)
