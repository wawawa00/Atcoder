import sys
from itertools import permutations
data = iter(sys.stdin.read().split())

N = int(next(data))
A = [[int(next(data)) for _ in range(N)] for _ in range(N)]
M = int(next(data))
uwasa = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    Xi = int(next(data))
    Yi = int(next(data))
    uwasa[Xi-1][Yi-1] = 1
    uwasa[Yi-1][Xi-1] = 1

mintime = float("inf")
for P in list(permutations(list(range(N)))):
    time = 0
    bool = False
    #print(P)
    #print(mintime)
    for i in range(N-1):
        if uwasa[P[i]][P[i+1]] == 1:
            bool = True
            break
        else:
            #print(time)
            time += A[P[i]][i]
    time += A[P[N-1]][N-1]
    #print(time)
    
    if time <= mintime and not bool:
        mintime = time

if mintime == float("inf"):
    print(-1)
else:
    print(mintime)