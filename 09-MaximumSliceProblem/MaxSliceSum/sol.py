def solution(A):
    n = len(A)
    best_to_here = [0]*n
    best_to_here[0] = A[0]
    for idx, val in enumerate(A[1:], 1):
        if best_to_here[idx-1] < 0:
            best_to_here[idx] = val
        else: 
            best_to_here[idx] = best_to_here[idx-1] + val 
    return max(best_to_here)
