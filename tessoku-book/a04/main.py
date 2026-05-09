import sys
def solve():
    data = sys.stdin.read().split()
    if not data: return

    N = int(data[0])

    answer = ["0"]*10

    for i in range(10):
        if N % 2 == 1:
            answer[9 - i] = "1"
            N = N // 2
        else:
            N = N // 2
    
    print("".join(answer))

if __name__ == '__main__':
    solve()