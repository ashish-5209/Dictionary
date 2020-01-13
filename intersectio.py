def intersection(arr1, arr2, n, m):
    res = 0
    for i in range(n):
        flag = False
        for j in range(i):
            if arr1[j] == arr1[i]:
                flag = True
                break

        if flag == True:
            continue
        for j in range(m):
            if arr1[i] == arr2[j]:
                print(arr1[i], end=" ")
                res += 1
                break
    print()
    return res

def intersection1(arr1, arr2, n, m):
    res = 0
    s = set()
    for i in range(n):
        s.add(arr1[i])
    for i in arr2:
        if i in s:
            res += 1
            print(i, end=" ")
            s.remove(i)
    print()
    return res

arr1 = [10,15,20,15,30,30,5]
arr2 = [30,5,30,80]
print(intersection(arr1, arr2, len(arr1), len(arr2)))
print(intersection1(arr1, arr2, len(arr1), len(arr2)))
