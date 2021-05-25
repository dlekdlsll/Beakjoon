inin = input()
inin = list(inin)
answer = []
result = 0

for i in inin:
    if i in('A','B','C'):
        answer.append(3)
    elif i in ('D','E','F'):
        answer.append(4)
    elif i in ('G','H','I'):
        answer.append(5)
    elif i in ('J','K','L'):
        answer.append(6)
    elif i in ('M','N','O'):
        answer.append(7)
    elif i in ('P','Q','R','S'):
        answer.append(8)
    elif i in ('T','U','V'):
        answer.append(9)
    elif i in ('W','X','Y','Z'):
        answer.append(10)
    elif i == '1':
        answer.append(2)
    elif i == '0':
        answer.append(11)
for i in answer:
    result += i
print(result)