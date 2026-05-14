import sys

data = iter(sys.stdin.read().split())

N, A, B, C = map(int, [next(data) for _ in range(4)])

def solve():
    ans = 9999
    for i in range(10000):
        for j in range(10000 - i):
            diff = N - (A*i + B*j)
            if diff >= 0 and diff % C == 0:
                k = diff // C
                if i + j + k <= 9999:
                    ans = min(ans, i+j+k)

    
    return print(ans)
                    

if __name__ == "__main__":
    solve()