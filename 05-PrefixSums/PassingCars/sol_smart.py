def solution(A):
    east_cars = 0
    total_passes = 0

    for car in A:
        if car == 0:
            east_cars += 1
        else:
            total_passes += east_cars
            if total_passes > 1_000_000_000:
                return -1

    return total_passes