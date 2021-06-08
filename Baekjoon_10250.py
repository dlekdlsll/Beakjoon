import sys

case = int(sys.stdin.readline())
room = []
rrn = ''

for i in range(0,case):
    h, w, n = map(int,sys.stdin.readline().split())
    cmd = n%h
    bbh = (n//h)+1

    if h == 1:
        cmd = 1
        bbh = n

    elif n % h == 0:
        cmd = h
        bbh = n//h
        
    if bbh<10:
        rrn ='0'+str(bbh)
    else :
        rrn = str(bbh)

    room.append((str(cmd)+rrn))

[print(a) for a in room]