def solution(A):
    A.sort()
    max1 = A[-1]
    max2 = A[-2]
    max3 = A[-3]
    min1 = A[0]
    min2 = A[1]

    return max(max1*max2*max3, min1*min2*max1)