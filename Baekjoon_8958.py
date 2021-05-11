N = int(input())
P = []
A = []
j = 0
for i in range(0,N): # 입력받을 줄의 개수
    T = input()
    A.append(T) # 리스트로 변환한 입력 = [ox결과1, ox결과2, ox결과3, ...]
# print('리스트A의 타입 :' ,type(A), '리스트A',A)

# print('len(A)', len(A), '= 입력받은 줄 수!')
# print(range(0,len(A))) # 0~입력받은 줄 수 ex) [0, 1, 2, 3, ...]
for k in range(0,len(A)): # 2줄입력받으면 2번도는 for문
    for a in range(0,len(A[k])): # A의 첫 번째 요소 = 'OO'
        # print(A[k][a]) # A의 첫 번째 요소(문자열)의 첫 번째 문자!
        if A[k][a] == 'O':
            j += 1
            P.append(j)    
            # print('리스트 P = ',P)
        else :
            j = 0
            P.append(j)
            # print('리스트 P = ',P)
    print(sum(P))
    j = 0
    P = []
# [print(q) for q in ]