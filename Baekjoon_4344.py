C = int(input())
s = []
R_sum = 0
for c in range(0,C):
    R = input().split()
    P = int(R[0])
    for p in range(0,P):
        k = 0
    for r in range(0,len(R[1:])):
        R_sum += int(R[r+1])
    if R_sum/P < int(R[p+1]) : k += 1
    s.append((k/P)*100)
    k = 0
    R_sum = 0
for i in range(0,len(s)):
    print('{0:0.3f}%'.format(round(s[i],3)))