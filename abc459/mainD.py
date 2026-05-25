import sys
import heapq
from collections import Counter

def modosu(hq, hq1, hq2):
    if hq1[0] == 0:
        heapq.heappush(hq, hq2)
    elif hq2[0] == 0:
        heapq.heappush(hq, hq1)
    else:
        heapq.heappush(hq, hq1)
        heapq.heappush(hq, hq2)
        
    


def solve():
    data = iter(sys.stdin.read().split())
    if not data: return
    T = int(next(data))
    for _ in range(T):
        S = next(data)
        n = len(S)
        counter = Counter(S)
        hq = []

        for char, count in counter.items():
            heapq.heappush(hq, [-count, char])
        nonei = []

        if -hq[0][0] > (len(S)+1)//2:
            print("No")
        
        else:
            while len(nonei) < n - 1:
                hq1 = heapq.heappop(hq)
                hq2 = heapq.heappop(hq)
                if len(nonei) == 0:
                    nonei.append(hq1[1])
                    hq1[0] += 1
                    modosu(hq, hq1, hq2)
                elif nonei[-1] != hq1[1]:
                    nonei.append(hq1[1])
                    hq1[0] += 1
                    modosu(hq, hq1, hq2)
                else:
                    nonei.append(hq2[1])
                    hq2[0] += 1
                    modosu(hq, hq1, hq2)
            if len(hq) >0:
                hq1 = heapq.heappop(hq)
                nonei.append(hq1[1])
            print("Yes")
            print("".join(nonei))

    

if __name__ == '__main__':
    solve()