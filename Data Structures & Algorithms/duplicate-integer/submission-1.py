class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for x in nums: 
            if x not in dic: 
                dic[x] = 1
            else: 
                dic[x] += 1 
        for i in dic:
            if dic[i] > 1:
                return True
        return False