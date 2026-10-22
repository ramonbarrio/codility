def solution(A):
    m = len(A) + 1
    expected_sum = m * (m + 1) // 2
    return expected_sum - sum(A)

# def solution(A):
#     return (set(range(1, len(A) + 2)) - set(A)).pop()