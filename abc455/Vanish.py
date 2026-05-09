import sys
import collections

def solve():
    data = iter(sys.stdin.read().split())
    N = int(next(data))
    K = int(next(data))

    A = [int(next(data)) for _ in range(N)]

    A_after = collections.Counter(A).most_common()
    B = [x[0]*x[1] for x in A_after]
    B_sorted = sorted(B)
    C = B_sorted[:len(B_sorted)-K]
    sum = 0
    for x in C:
        sum += int(x)
    if len(B_sorted)< K:
        print(0)
    else:
        print(int(sum))


        


if __name__ == "__main__":
    solve()

