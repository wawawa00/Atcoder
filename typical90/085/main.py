import sys
import math


data = iter(sys.stdin.read().split())

K = int(next(data))
a_choise=math.ceil(math.pow(K, 1/3))

count = 0

for i in range(1, a_choise+1):
    if K % i != 0:
        continue
    b_choise=math.ceil(math.pow(K/i, 1/2))
    for j in range(i, b_choise+1):
        c_choise=-(-K//(i*j))
        if K % j != 0:
            continue
        k = int(K/(i*j))
        if j <= k <= c_choise:
            
            
            if i*j*k == K:
                count += 1

print(count)