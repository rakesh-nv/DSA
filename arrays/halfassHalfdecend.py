

arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
n = len(arr)
arr.sort()

i = 0
while i < n//2:
    print(arr[i],end=' ')
    i = i+1

j = n-1
while j>=n//2:
    print(arr[j],end=' ')
    j = j-1