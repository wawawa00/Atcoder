import sys

def binary_search(sorted_list, search_value):
    left_index = 0
    right_index = len(sorted_list) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = sorted_list[middle_index]

        if search_value == middle_value:
            return 0
        if search_value < middle_value:
            right_index = middle_index - 1
        if search_value > middle_value:
            left_index = middle_index + 1
    mini = float('inf')
    if right_index >= 0:
        mini = abs(sorted_list[right_index] - search_value)
    if left_index < len(sorted_list):
        mini = min(mini, abs(sorted_list[left_index] - search_value))
    return mini

def solve():
    data = iter(sys.stdin.read().split())
    if not data: return

    N = int(next(data))
    A = [int(next(data)) for _ in range(N)]
    A_sorted = sorted(A)
    Q = int(next(data))

    for j in range(Q):
        B_j = int(next(data))
        opt = binary_search(A_sorted, B_j)
        print(opt)

if __name__ == '__main__':
    solve()