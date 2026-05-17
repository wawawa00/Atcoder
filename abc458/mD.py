import sys
import heapq
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    X = int(next(data))
    Q = int(next(data))
    left_hq = []
    right_hq = []
    mid = X

    for _ in range(Q):
        
        Ai = int(next(data))
        Bi = int(next(data))
        if Ai <= mid <= Bi:
            heapq.heappush(left_hq, -Ai)
            heapq.heappush(right_hq, Bi)
            print(mid)
        elif Bi <= mid <= Ai:
            heapq.heappush(left_hq, -Bi)
            heapq.heappush(right_hq, Ai)
            print(mid)
        elif Bi < mid and Ai < mid:
            heapq.heappush(left_hq, -Ai)
            heapq.heappush(left_hq, -Bi)
            heapq.heappush(right_hq, mid)
            mid = - heapq.heappop(left_hq)
            print(mid)
        elif mid < Ai and mid < Bi:
            heapq.heappush(right_hq, Ai)
            heapq.heappush(right_hq, Bi)
            heapq.heappush(left_hq, -mid)
            mid = heapq.heappop(right_hq)
            print(mid)
        
        



if __name__ == '__main__':
    solve()