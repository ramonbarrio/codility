def solution(A, B, K):
    if A % K == 0:
        first_mult = A
    else:
        first_mult = (A // K + 1)*K
    span = B - first_mult
    return span // K + 1