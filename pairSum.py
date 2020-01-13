def pair(arr, sum):
    s = set()
    for i in arr:
        if (sum-i) in s:
            return True
        s.add(i)
    return False

def pair1(arr, sum):
    for i in range(len(arr)):
        for j in range(i+1, n):
            if (arr[i]+arr[j]) == sum:
                return True
    return False

arr = [3,2,8,15,-8]
sum = 17
print(pair(arr, sum))
print(pair(arr, sum))
