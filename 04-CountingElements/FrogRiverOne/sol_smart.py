def solution(X, A):
    if len(A) < X:
        return -1

    covered = set()
    for t, pos in enumerate(A):
        covered.add(pos)
        if len(covered) == X:
            return t

    return -1