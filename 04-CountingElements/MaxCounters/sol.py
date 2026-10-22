def solution(N, A):
    counter = [0]*N
    curr_max = 0
    curr_floor = 0
    
    for el in A:
        if el > N:
            curr_floor = curr_max
        else:
            if counter[el - 1] < curr_floor:
                counter[el - 1] = curr_floor + 1
            else:
                counter[el - 1] += 1
            curr_max = max(curr_max, counter[el - 1])

    for idx, el in enumerate(counter):
        if el < curr_floor:
            counter[idx] = curr_floor
    
    return counter