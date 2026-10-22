def solution(A):
    n = len(A)
    seen = set()
    for el in A:
        if el < 1 or el > n or el in seen:
            return 0
        seen.add(el)
    return 1

# def solution(A):
#     return int(max(A) == len(A) == len(set(A)))