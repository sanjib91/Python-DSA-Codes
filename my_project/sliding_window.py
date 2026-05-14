def max_sum_subarray(arr, k):
    s = sum(arr[:k])
    m = s
    for i in range(k, len(arr)):
        s += arr[i] - arr[i-k]
        m = max(m, s)
    return m