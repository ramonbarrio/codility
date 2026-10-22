def solution(A, B):
    alive = 0
    downstream_stack = []
    for size, stream in zip(A, B):
        if stream == 1:
            downstream_stack.append(size)
        else:
            while True:
                if not downstream_stack:
                    alive += 1
                    break
                elif downstream_stack[-1] > size:
                    break
                else:
                    downstream_stack.pop()

    return alive + len(downstream_stack)