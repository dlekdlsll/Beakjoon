A ,B = input().split()
A,B = str(A),str(B)
li_A,li_B = [],[]

for i in A:
    li_A.insert(0,i)
for i in B:
    li_B.insert(0,i)

A,B = '',''

for i in li_A:
    A = A + i

for i in li_B:
    B = B + i

A, B = int(A), int(B)

if A>B :    
    print(A)
else:
    print(B)