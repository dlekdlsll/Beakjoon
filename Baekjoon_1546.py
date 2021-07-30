N = int(input())
O = input().split()
for i in range(0,N):
    O[i] = (int(O[i]))
J = [k/max(O)*100 for k in O]
print(sum(J)/N)
# 테스트 중입니다...