import sys
def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    Q = int(next(data))
    is_prime = [True]*(10**5+1)
    is_prime[0] = is_prime[1] = False
    is_2017 = [False]*(10**5+1)
    for i in range(len(is_prime)):
        if is_prime[i]:
            if i % 2 == 1 and is_prime[int((i+1)/2)]:
                is_2017[i] = True
            #print(i)
            for j in range(i*2, len(is_prime), i):
                is_prime[j] = False
    
    count_2017 = []
    count = 0
    for i in range(len(is_2017)):
        if is_2017[i]:
            count += 1
        count_2017.append(count)
    for i in range(Q):
        li = int(next(data))
        ri = int(next(data))
        print(count_2017[ri]-count_2017[li-1])

if __name__ == '__main__':
    solve()