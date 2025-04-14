

arr1 = [3, 5, 2, 5, 2, 0, 9, 4]
arr2 = [1, 5, 2, 1, 2, 3, 9, 4]
arr3 = [3, 5, 2, 6, 5, 3, 9, 4, 4]

common = []

for i in arr1:
    if i in arr2 and i in arr3:
        common.append(i)

print(list(set(common)))