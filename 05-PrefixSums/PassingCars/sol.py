def solution(A):
    n = len(A)
    pref = [0]*n
    pref[0] = A[0]
    
    total_passes = 0

    for i in range(1, n):
        pref[i] = pref[i-1]+A[i]
    # print(pref)
    
    total_cars_west = pref[-1]

    for idx, car in enumerate(A):
        if car == 0:
            total_passes += (total_cars_west-pref[idx])
            if total_passes > 1e9:
                return -1

    return total_passes