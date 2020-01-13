def zero(arr, n):
    s = set()
    prefix_sum = 0

    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum in s or prefix_sum == 0:
            return True
        s.add(prefix_sum)
    return False

def zero1(arr, n):
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == 0:
                return True
    return False

arr = [1,4,13,-3,-10,5]
print(zero(arr, len(arr)))
print(zero1(arr, len(arr)))
