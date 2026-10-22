def solution(A):
    n = len(A)
    least_avg = float('inf')
    idx = -1
    for P in range(n-2):
        curr_avg_2 = (A[P] + A[P+1])/2
        curr_avg_3 = (A[P] + A[P+1] + A[P+2])/3
        if curr_avg_2 < least_avg or curr_avg_3 < least_avg:
            idx = P
            least_avg = min(curr_avg_2, curr_avg_3)
    curr_avg_2 = (A[-1] + A[-2])/2
    if curr_avg_2 < least_avg:
        return n-2
    return idx