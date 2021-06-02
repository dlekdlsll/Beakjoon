N = int(input())
i = 2
times = 1
answer = 0

if N == 1:
    answer = 1

else:
    while True:
        if N <= (6*times)+1:
            break
        times += i
        i += 1
    answer = i
print(answer)