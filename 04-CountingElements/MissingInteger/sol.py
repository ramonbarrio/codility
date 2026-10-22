def solution(A):
    seen = set()
    smallest = 1
    for val in A:
        if val > 0:
            seen.add(val)
    while smallest in seen:
        smallest += 1
    
    return smallest