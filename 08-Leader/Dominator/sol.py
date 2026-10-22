def solution(A):
    n = len(A)
    vals_dic = {}
    vals_idx = {}
    for idx, val in enumerate(A):
        vals_dic[val] = vals_dic.get(val, 0) + 1 
        vals_idx[val] = idx
    for val in vals_dic:
        if vals_dic[val] > n//2:
            return vals_idx[val]
    return -1 