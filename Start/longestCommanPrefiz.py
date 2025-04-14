class Solution(object):
    def longestCommonPrefix(self, strs):
      
        if len(strs)==0:
            return ""
        
        base = strs[0]
        lb=len(base)
        for i in range(lb):
            for word in strs[1:]:
               if i== len(word) or word[i] != base[i]:
                    return base[0:i]
        return base
      
solution = Solution()
strs = ["flower","flow","flight"]
print(solution.longestCommonPrefix(strs))