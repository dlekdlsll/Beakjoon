K = [int(input()) for i in range(0,10)]
K2 = {K[j]%42 for j in range(len(K))}
print(len(K2))