

# using hash table to solve the problem

# Time complexity: O(n)

# return the index which 2 sum is equeal to 4

class Solution:
    def twoSom(self, nums:list[int],target:int):
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target -n 
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return

solution = Solution()
print(solution.twoSom([2,1,5,3],4)) # [1,3]