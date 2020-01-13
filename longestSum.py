def longest(arr, n, sum):
    d = {}
    prefix_sum = 0
    res = 0

    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum == sum:
            res = i+1
        if prefix_sum not in d:
            d[prefix_sum] = i
        if prefix_sum - sum in d:
            res = max(res, i - d[prefix_sum-sum])
    return res

arr = [8,3,1,5,-6,6,2,2]
sum = 4
print(longest(arr, len(arr), sum))
