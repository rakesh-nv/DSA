
#find closest num in array
#[2, -1, 1]



def findClosestNum(nums):
    closest = nums[0]

    # time complexity is O(n)
    for x in nums:
        if abs(x) < abs(closest):
            closest = x

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest
    
nums=[7,2, -2, 5,1]

result = findClosestNum(nums)

print(result)







