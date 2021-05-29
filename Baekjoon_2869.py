import sys
import math

A, B, V = map(int,sys.stdin.readline().split())
 
answer = (V/(A-B) - A) + 1
print(answer)
print(abs(math.ceil(answer)))
