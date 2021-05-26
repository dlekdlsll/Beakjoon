inin = str(input())
CA = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
solve = 0

for i in range(0,len(CA)):
    if inin.count(CA[i]) > 0:
        solve += inin.count(CA[i])
    inin = inin.replace(CA[i]," ")
inin = inin.replace(" ","")

answer = len(inin)+solve
print(answer)