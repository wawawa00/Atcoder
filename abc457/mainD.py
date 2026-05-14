import sys
import math

data = iter(sys.stdin.read().split())
N = int(next(data))
K = int(next(data))
A = [int(next(data)) for _ in range(N)]

def isok(x):
    count = 0
    for index, value in enumerate(A, start=1):
        if value < x:
            count += -(-(x-value)//index)
            if count > K:
                return False
    return True

left = 1
right = A[0] + K + 1

while left+1<right:
    m = (left+right)//2
    if isok(m):
        left = m
    else:
        right = m

print(left)