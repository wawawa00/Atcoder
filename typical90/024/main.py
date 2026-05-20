import sys

data = iter(sys.stdin.read().split())

N = int(next(data))
K = int(next(data))
A = [int(next(data)) for _ in range(N)]
B = [int(next(data)) for _ in range(N)]

C = [abs(A[i] - B[i]) for i in range(N)]
diff = sum(C)

if diff - K <= 0 and (diff - K) % 2 == 0:
    print("Yes")
else:
    print("No")