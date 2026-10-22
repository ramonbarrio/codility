from itertools import accumulate


def solution(S, P, Q):
    """GenomicRangeQuery in O(N + M) time, O(N) extra space.

    For each of A, C, G we keep a prefix count: prefix[i] = occurrences in S[:i].
    A nucleotide is present in S[p..q] (inclusive) iff prefix[q + 1] - prefix[p] > 0.
    Check A, C, G in order of impact; if none is present, the minimum must be T (4).
    """
    prefixes = [list(accumulate((ch == n for ch in S), initial=0)) for n in "ACG"]

    result = []
    for p, q in zip(P, Q):
        for impact, prefix in enumerate(prefixes, start=1):
            if prefix[q + 1] > prefix[p]:
                result.append(impact)
                break
        else:
            result.append(4)
    return result


if __name__ == "__main__":
    import random
    import time

    # Example from the task statement
    assert solution("CAGCCTA", [2, 5, 0], [4, 5, 6]) == [2, 4, 1]

    # Cross-check against brute force on random small inputs
    impact = {"A": 1, "C": 2, "G": 3, "T": 4}
    for _ in range(2000):
        n = random.randint(1, 30)
        s = "".join(random.choice("ACGT") for _ in range(n))
        m = random.randint(1, 20)
        p = [random.randrange(n) for _ in range(m)]
        q = [random.randint(pi, n - 1) for pi in p]
        expected = [min(impact[c] for c in s[a:b + 1]) for a, b in zip(p, q)]
        assert solution(s, p, q) == expected, (s, p, q)

    # Worst case for Codility limits: N = 100,000, M = 50,000, full-range queries
    s = "T" * 100_000
    p, q = [0] * 50_000, [99_999] * 50_000
    t = time.perf_counter()
    solution(s, p, q)
    print(f"all tests passed; max-size run took {time.perf_counter() - t:.3f}s")
