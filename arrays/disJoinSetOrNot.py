

# if elements in arr1 not in array2 Then it is calles disjoint set

arr1 = [12, 34, 11, 9, 3]
arr2 = [7, 2, 1, 5,]
isdisjoint = 1
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if(arr1[i]==arr2[j]):
            isdisjoint =0
            break

if isdisjoint == 1:
    print("disjoint")
else:
    print("not disjoint")
     
    
