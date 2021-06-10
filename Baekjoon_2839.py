N = int(input())
Kg5,Kg3 = 0,0

while True:
    if N < 5 and N!=3 :
        Kg5= -1; Kg3= 0
        break
    if N%5!=0:
        N -= 3; Kg3 += 1
        if N == 0: break
    if N%5==0:
        N -= 5; Kg5 += 1
        if N == 0: break
print(Kg5+Kg3)