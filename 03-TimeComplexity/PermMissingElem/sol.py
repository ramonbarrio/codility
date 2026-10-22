def solution(A):
    N = len(A) + 1
    complete_range = set(range(1,N+1))
    for i in A:
        complete_range.discard(i)
    return complete_range.pop()