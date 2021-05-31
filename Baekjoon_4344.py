times = int(input())
answer = []

for i in range(0,times):
    case = list(map(int,input().split()))
    student = case[0]
    aver = sum(case[1:])/student
    result = 0
    for j in range(1,len(case)):
        if case[j] > aver:
            result += 1
    answer.append(result/student*100)

for i in answer:
    print('{0:0.3f}%'.format(round(i,3)))