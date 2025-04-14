

arr1 = [11, 12, 13, 21, 30, 70]
arr2 = [11, 30, 70, 12]

isSubset = 1
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr2[i] in arr1:
            continue
        else:
            isSubset = 0


print(isSubset)