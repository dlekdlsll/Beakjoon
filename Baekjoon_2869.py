import sys
import math

A, B, V = map(int,sys.stdin.readline().split())
V = V-A
answer = (V/(A-B)) + 1
print(math.ceil(answer))