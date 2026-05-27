import sys
from collections import Counter
data = iter(sys.stdin.read().split())
N = int(next(data))
A = [int(next(data)) for _ in range(N)]
B = [int(next(data)) for _ in range(N)]
C = [int(next(data)) for _ in range(N)]

A_amari = Counter([x%46 for x in A])
B_amari = Counter([x%46 for x in B])
C_amari = Counter([x%46 for x in C])
count = 0
for key_A in A_amari.keys():
    for key_B in B_amari.keys():
        for key_C in C_amari.keys():
            if (key_A + key_B + key_C) % 46 == 0:
                #print("Yes")
                count += A_amari[key_A]*B_amari[key_B]*C_amari[key_C]
print(count)