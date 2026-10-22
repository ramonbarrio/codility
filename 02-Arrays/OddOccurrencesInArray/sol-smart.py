def solution(A):
    unpaired = set()
    for item in A:
        if item in unpaired:
            unpaired.remove(item)  # O(1) average lookup & removal
        else:
            unpaired.add(item)     # O(1) average insertion
    return unpaired.pop()          # Only the unpaired element is left