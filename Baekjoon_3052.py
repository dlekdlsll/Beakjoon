K = [int(input()) for i in range(0,10)]
K2 = [K[j]%42 for j in range(len(K))]
K3 = list(set(K2))    # 비파괴적 함수 : 새로운 변수 저장 필요
print(len(K3))