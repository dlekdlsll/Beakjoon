S = input()
Test = 'abcdefghijklmnopqrstuvwxyz'
for t in range(0,len(Test)):
    if S.count(Test[t]) > 0:
        print(S.find(Test[t]),end = ' ')
    else:
        print(-1,end =' ')