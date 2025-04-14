
import math

arr = [10, 80, 9,56, 4,80,8,90]

first_small=math.inf
secont_small=math.inf

for i in range(len(arr)):
    if arr[i] < first_small:
        first_small = arr[i]

for i in range(len(arr)):
    if arr[i] !=first_small and arr[i] < secont_small:
        secont_small = arr[i]

print(secont_small)
print(first_small)
