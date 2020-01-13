def isSubset(arr1, arr2):

    s = set()

    for i in arr1:
        s.add(i)

    for i in arr2:
        if i not in s:
            return False
    return True

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

print(isSubset(arr1, arr2))
