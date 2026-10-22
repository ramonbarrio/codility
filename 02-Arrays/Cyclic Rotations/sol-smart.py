def solution(A, K):
    n = len(A)
    if n == 0:
        return A
    k = K % n
    if k == 0:
        return A

    def reverse(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    reverse(A, 0, n - 1)  # 1. Reverse whole array
    reverse(A, 0, k - 1)  # 2. Reverse first k elements
    reverse(A, k, n - 1)  # 3. Reverse remaining n - k elements
    return A