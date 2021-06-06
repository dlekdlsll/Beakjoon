N = int(input())
answer = 0

if N % 5 > 1 and N//5 > 1 :
    namergy = N%5
    if namergy%3==0:
        answer = (N//5 + namergy//3)
elif N % 3 > 1 and N//3 > 1 :
    namergy = N%3
    if namergy%5==0:
        answer = (N//3 + namergy//5)
elif N % 3 == 0:
    answer = N//3
elif N % 3 == 2:
    answer = ((N - 5)/3) + 1
else:
    answer = -1

print(int(answer))