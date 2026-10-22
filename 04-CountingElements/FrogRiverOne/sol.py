def solution(X, A):
    pos_set = set(range(1, X+1))
    for t in range(len(A)):
        pos_set.discard(A[t])
        if not pos_set:
            return t
    return -1