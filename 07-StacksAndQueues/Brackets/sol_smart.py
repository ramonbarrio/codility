def solution(S):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in S:
        if char in pairs:
            # Closer must match the most recent unmatched opener
            if not stack or stack.pop() != pairs[char]:
                return 0
        else:
            stack.append(char)
    return int(not stack)
