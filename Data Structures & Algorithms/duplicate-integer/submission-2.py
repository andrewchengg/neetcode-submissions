class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {} 
        for i in nums:
            if i not in seen: 
                seen[i] = 1 
            else:
                if i in seen:
                    return True
        return False 
        


        