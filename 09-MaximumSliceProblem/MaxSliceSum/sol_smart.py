from itertools import islice


def solution(A):
    best_ending_here = A[0]  # best sum of a slice ending at the current index
    best_overall = A[0]
    for val in islice(A, 1, None):  # skips A[0] without copying the list
        # Extend the previous slice, or start fresh if it only drags us down
        best_ending_here = max(val, best_ending_here + val)
        best_overall = max(best_overall, best_ending_here)
    return best_overall
