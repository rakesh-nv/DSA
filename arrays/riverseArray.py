

arr = [10, 20, 30, 40, 50]

stare = 0
last = len(arr) - 1

while stare < last:
    temp = arr[stare]
    arr[stare] = arr[last]
    arr[last] = temp
    staret = stare + 1
    last = last - 1
    

print(arr)

