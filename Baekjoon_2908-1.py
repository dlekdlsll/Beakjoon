A, B = input().split()
A, B = str(A), str(B)
A = A[::-1]
B = B[::-1]
A, B = int(A), int(B)
if A > B:
    print(A)
else:
    print(B)