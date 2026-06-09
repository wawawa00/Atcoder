import sys


def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    S = next(data)
    K = int(next(data))

    left = 0
    countdot = 0
    ans = 0

    for right in range(len(S)):
        if S[right] == '.':
            countdot += 1

        while countdot > K:
            if S[left] == '.':
                countdot -= 1
            left += 1
        #print(left, right)
        ans = max(ans, right - left + 1)
    print(ans)
if __name__ == '__main__':
    solve()