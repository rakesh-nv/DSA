# find the subarray with max sum


arr = [-2,-3,4,-1,-2,1,5,-3]
max = -999
sum =0
for i in arr:
    sum = sum + i
    if sum > max:
        max = sum
        print(i,end=" ")
    if sum < 0:
        sum = 0
print(" ")        
print(max)





# # max poduct of subarray
# arr = [1, -2, -3, 0, 7, -8, -2]
# max_product = arr[0]
# min_product = arr[0]
# result = arr[0]

# for i in range(1,len(arr)):
#     if arr[i]<0:
#         max_product,min_product = min_product,max_product

#     max_product = max(arr[i],arr[i]*max_product)
#     min_product = min(arr[i],arr[i]*min_product)
#     result = max(result,max_product)
# print(result)

    




