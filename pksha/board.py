def solution(A):
    A.sort()
    N = len(A)

    if N <= 1:
        return 1

    ans = A[-1] - A[0]  # 1枚で全部覆う場合より悪くはならない

    for i in range(N - 1):
        # 左側: A[0] 〜 A[i]
        left_len = A[i] - A[0]

        # 右側: A[i+1] 〜 A[N-1]
        right_len = A[-1] - A[i + 1]

        # 2枚は同じ長さなので、大きい方に合わせる
        L = max(left_len, right_len)

        ans = min(ans, L)

    # 長さは正の整数なので、0なら1にする
    return max(1, ans)