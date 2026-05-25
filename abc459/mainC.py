import sys
from collections import defaultdict
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    Q = int(next(data))
    
    count = 0
    block_index = defaultdict(int) # インデックスに積まれているブロックの数
    block_number = defaultdict(int) # i個以上のブロックが積まれているインデックスの数
    block_number[0] = N

    for _ in range(Q):
        query0 = int(next(data))
        query1 = int(next(data))

        if query0 == 1:
            a = block_index[query1]
            block_number[a+1] += 1
            block_index[query1] = a+1
            if block_number[count+1] == N:
                count += 1
        else:
            print(block_number[query1+count])



        
            

if __name__ == '__main__':
    solve()