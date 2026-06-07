class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        indicator = None 
        temp = {}
        for i in range(1,len(nums)):
            prev = nums[i-1]
            curr = nums[i] 
            if prev == curr:
                continue 
            if (prev + 1) == curr:
                if indicator is None: 
                    indicator = curr 
                if indicator not in temp:
                    temp[indicator] = 1
                temp[indicator] += 1 
            if (curr - prev) > 1:
                indicator = None
        result = []
        for key, value in temp.items(): 
            result.append(value)
        if not result: 
            return 1
        return max(result)
            
        
            
            
                