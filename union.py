def union(arr1, arr2, n, m):
    res = 0
    arr = [0]*(m+n)

    for i in range(n):
        arr[i] = arr1[i]
    for i in range(m):
        arr[n+i] = arr2[i]

    for i in range(m+n):
        flag = False
        for j in range(i):
            if arr[i] == arr[j]:
                flag = True
                break
        if flag == False:
            res += 1
            print(arr[i], end=" ")
    print()
    return res

def union1(arr1, arr2, n, m):
    s = set()
    for i in range(n):
        s.add(arr1[i])
    for i in range(m):
        s.add(arr2[i])
    return len(s)

arr1 = [15,20,5,15]
arr2 = [15,15,15,20,10]
print(union(arr1, arr2, len(arr1), len(arr2)))
print(union1(arr1, arr2, len(arr1), len(arr2)))
