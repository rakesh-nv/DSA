

arr = [7,2, -2, 5,1,10]

small = arr[0]
large = arr[0]

for i in range(len(arr)):
    if arr[i] < small:
        small = arr[i]

    if arr[i] > large:
        large = arr[i]

print(small)
print(large)