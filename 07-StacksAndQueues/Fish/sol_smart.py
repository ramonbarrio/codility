def solution(A, B):
    alive_upstream = 0
    downstream = []  # sizes of downstream fish still alive, nearest on top

    for size, direction in zip(A, B):
        if direction == 1:
            downstream.append(size)
        else:
            # Upstream fish eats every smaller downstream fish in front of it
            while downstream and downstream[-1] < size:
                downstream.pop()
            if not downstream:
                alive_upstream += 1

    return alive_upstream + len(downstream)
