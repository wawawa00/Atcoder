import sys 
data = iter(sys.stdin.read().split())

def make_binary_list(N):
    binary_list = [[int(bit) for bit in format(i, 'b').zfill(N)] for i in range(2**N)]
    return binary_list

def solve():
    N=int(next(data))

    if N % 2 == 0:
        array = make_binary_list(N)
        array_correct = []

        for x in array:
            count = 0
            bool = True
            for i in range(N):

                if count < 0:
                    bool = False
                    break
                    
                else:
                    if x[i] == 0:
                        count += 1
                    else:
                        count -= 1
            if count != 0 or not bool:
                continue
            else:
                array_correct.append(x)
    
        for x in array_correct:
            for i in range(N):
                if x[i] == 0:
                    x[i] = "("
                else:
                    x[i] = ")"
            
            print("".join(x))
    else:
        print()


if __name__ == "__main__":
    solve()