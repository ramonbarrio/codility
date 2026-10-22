def solution(A):
    curr_least_diff = float('inf')
    curr_diff = -sum(A)
    for i in range(len(A) - 1):
        curr_diff += 2 * A[i]
        diff = abs(curr_diff)
        curr_least_diff = min(curr_least_diff, diff)
    return curr_least_diff