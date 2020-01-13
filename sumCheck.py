def sum1(arr, n, sum):
    s = set()
    prefix_sum = 0

    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum - sum in s or prefix_sum == sum:
            return True
        s.add(prefix_sum)
    return False

def sum2(arr, n, sum):
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == sum:
                return True
    return False

arr = [8,3,1,5,-6,6,2,2]
sum = 4
print(sum1(arr, len(arr), sum))
print(sum2(arr, len(arr), sum))
