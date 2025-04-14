
#find closest num in array
#[2, -1, 1]



def findClosestNum(nums):
    smallest = nums[0]

    # time complexity is O(n)
    for x in nums:
        if x < smallest:
            smallest = x
            
    return smallest
    
nums=[7,2, -2, 5,1,10]

result = findClosestNum(nums)

print(result)







