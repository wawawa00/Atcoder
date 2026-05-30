from collections import defaultdict

def solution(N, A, B):
    d = defaultdict(set)

    for i in range(len(A)):
        d[A[i]].add(B[i])
        d[B[i]].add(A[i])

    for v in range(1, N):
        if v + 1 not in d[v]:
            return False

    return True