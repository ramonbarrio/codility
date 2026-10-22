def solution (A, K):
    array_len = len(A)
    if array_len == 0:
        return A
    effective_K = K % array_len
    if effective_K == 0:
        return A
    return A[-effective_K:] + A[:-effective_K]


# def solution(A, K):
#     if not A:
#         return A
#     k = K % len(A)
#     return A[-k:] + A[:-k]