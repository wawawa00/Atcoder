import sys
import heapq
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    M = int(next(data))
    A = [int(next(data)) for _ in range(N)]
    B = [int(next(data)) for _ in range(M)]
    Aminus = list(map(lambda x: x*(-1), A))
    Bminus = list(map(lambda x: x*(-1), B))
    heapq.heapify(Aminus)
    heapq.heapify(Bminus)
    count = 0

    while len(Aminus) != 0 and len(Bminus) != 0:

        a = heapq.heappop(Aminus)*(-1)
        b = heapq.heappop(Bminus)*(-1)
        if 2*a >= b:
            count += 1
            #print("Yes")
            #print(a, b)
        else:
            #print("No")
            #print(a, b)
            #print(Aminus)
            heapq.heappush(Aminus, a*(-1))
            #print(Aminus)
    print(count)
    

    

if __name__ == '__main__':
    solve()