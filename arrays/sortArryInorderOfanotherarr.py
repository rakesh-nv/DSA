
from collections import Counter



def sort_by_order(arr1,arr2):
    count = Counter(arr1)
    result = []

    for num in arr2:
        if num in count:
            print([num]*count[num])
            result.extend([num] * count[num])
            del count[num]

    remaining = sorted(count.elements())

    result.extend(remaining)
    return result


# Input arrays
arr1 = [20, 1, 20, 5, 7, 1, 9, 39, 6, 18, 18]
arr2 = [20, 1, 18, 39]

# Sorting arr1 based on arr2 order
sorted_arr = sort_by_order(arr1, arr2)
print(sorted_arr)