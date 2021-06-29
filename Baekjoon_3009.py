X, Y = [],[]
for _ in range(3):    # 3번 반복합니다 # 진짜 푸쉬 되는건가 이제?
    x, y = map(int, input().split())
    X.append(x); Y.append(y)
for i in range(3):
    if X.count(X[i]) == 1: x2 = X[i]
    if Y.count(Y[i]) == 1: y2 = Y[i]
print(x2, y2)
