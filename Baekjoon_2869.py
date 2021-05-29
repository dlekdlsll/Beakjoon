import sys
import math

A, B, V = map(int,sys.stdin.readline().split())

if A == V:
    answer = 1
    print(answer)
else:
    answer = (V/(A-B) - A) + 1
    print(abs(math.ceil(answer)))