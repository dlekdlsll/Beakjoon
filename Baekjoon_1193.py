X = int(input())
step = 1
x = 1

while True:
    if x >= X :
        break
    step += 1
    x += step 

if step % 2 == 1:
    m = step-(x-X)
    s = (x-X) +1

else:
    m = (x-X) +1
    s = step-(x-X)

print("{0}/{1}".format(s,m))