def solution(A):
    n = len(A)
    full_set = set(range(1,n + 1))
    for el in A:
        full_set.discard(el)
    if not full_set:
        return 1
    return 0 