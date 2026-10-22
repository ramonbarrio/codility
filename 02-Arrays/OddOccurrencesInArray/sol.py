def solution(A):
    accounting = {}
    for val in A:
        accounting[val] = accounting.get(val, 0) + 1
    for val, count in accounting.items():
        if count % 2 == 1:
            return val