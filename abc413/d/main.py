import sys 
data = iter(sys.stdin.read().split())

def solve():
    T = int(next(data))
    for _ in range(T):
        N = int(next(data))
        A = [int(next(data)) for _ in range(N)]
        A_sorted = sorted(A, key=abs)
        a0 = abs(A_sorted[0])
        different = False

        for i in range(N):
            if abs(A_sorted[i]) != a0:
                different = True
                break
        if not different:
            cnt_pos = A.count(a0)
            cnt_neg = N - cnt_pos
            if cnt_pos == N or cnt_neg == N or abs(cnt_neg - cnt_pos) < 2:
                print("Yes")
            else:
                print("No")
            continue
        bool = True
        for i in range(N-1):
            if A_sorted[0] * A_sorted[i + 1] != A_sorted[1] * A_sorted[i]:
                bool = False
                break
        
        if bool:
            print("Yes")
        else:
            print("No")    

if __name__ == "__main__":
    solve()