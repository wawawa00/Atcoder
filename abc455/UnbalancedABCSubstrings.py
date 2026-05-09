import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    S = next(data)
    all = [[0, 0, 0] for _ in range(N)]

    count_a = 0
    count_b = 0
    count_c = 0

    for i in range(N):
        if S[i] == 'A':
            count_a += 1
        elif S[i] == 'B':
            count_b += 1
        else:
            count_c += 1
        all[i][0] = count_a
        all[i][1] = count_b
        all[i][2] = count_c


    

if __name__ == '__main__':
    solve()