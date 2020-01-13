def isPresent(arr, x):

    s = set()
    for i in arr:
        if x-i in s:
            return True
        s.add(i)

    return False

A = [1, 4, 45, 6, 10, 8]
n = 16
print(isPresent(A, n))
