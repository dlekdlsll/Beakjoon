K = [int(input()) for i in range(0,10)]
print(len({K[j]%42 for j in range(len(K))}))