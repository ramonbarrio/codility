def solution(N, A):
    counter = [0] * N
    curr_max = 0
    curr_floor = 0

    for el in A:
        if el > N:
            curr_floor = curr_max
        else:
            idx = el - 1
            if counter[idx] < curr_floor:
                counter[idx] = curr_floor + 1
            else:
                counter[idx] += 1

            if counter[idx] > curr_max:
                curr_max = counter[idx]

    for idx, val in enumerate(counter):
        if val < curr_floor:
            counter[idx] = curr_floor

    return counter