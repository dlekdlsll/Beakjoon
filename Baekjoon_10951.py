i = 1
while  19 > i and i > 0:
    try:
        A, B = map(int,input().split())
        i = (A+B)
        print(i)
    except EOFError:
        break