# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    n = len(S)
    pref_A = [0]*(n+1)
    pref_C = [0]*(n+1)
    pref_G = [0]*(n+1)
    pref_T = [0]*(n+1)

    for idx, gene in enumerate(S, 1):
        pref_A[idx] = pref_A[idx - 1] + int(gene == 'A')
        pref_C[idx] = pref_C[idx - 1] + int(gene == 'C')
        pref_G[idx] = pref_G[idx - 1] + int(gene == 'G')
        pref_T[idx] = pref_T[idx - 1] + int(gene == 'T')
    
    m = len(P)
    resp = [0]*m

    # print(pref_A)
    # print(pref_C)
    # print(pref_G)
    # print(pref_T)

    for idx, edges in enumerate(zip(P,Q)):
        if pref_A[edges[1]+1] > pref_A[edges[0]]:
            resp[idx] = 1
        elif pref_C[edges[1]+1] > pref_C[edges[0]]:
            resp[idx] = 2
        elif pref_G[edges[1]+1] > pref_G[edges[0]]:
            resp[idx] = 3
        else:
            resp[idx] = 4

    # print(resp)
    return resp
