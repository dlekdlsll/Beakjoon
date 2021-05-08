i = 1
s = []
while i > 0:
    A, B = map(int,input().split())
    i = (A+B)
    if i > 0:
        s.append(A+B)
for j in s:
    print(j)