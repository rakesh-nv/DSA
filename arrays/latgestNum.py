
arr = [10, 80, 9,56, 4,80,8,90]
max = arr[0]

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]

print("Largest number in the array is: ", max)