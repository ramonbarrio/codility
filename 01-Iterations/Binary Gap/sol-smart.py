def solution(N):
    # 1. Strip trailing zeros using bitwise trick (or a while loop)
    # N & -N isolates the lowest set bit; integer division shifts past trailing zeros
    N //= N & -N

    max_gap = 0
    current_gap = 0

    # 2. Scan remaining bits from right to left
    while N:
        if N & 1:
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
        else:
            current_gap += 1
        N >>= 1

    return max_gap