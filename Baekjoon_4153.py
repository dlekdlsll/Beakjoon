printout = []

while True:
    listinin = [int(x) for x in input().split()]
    if listinin.count(0)==3:
        break
    
    validation = [i**2 for i in listinin]
    validation.sort()
    A = validation[0]; B = validation[1]; C = validation[2]
    
    if (A+B) == C: printout.append("right")
    else: printout.append("wrong")
[print(x) for x in printout]