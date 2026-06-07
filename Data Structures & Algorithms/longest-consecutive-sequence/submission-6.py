class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set() 
        start = 0
        longest = 1
        for num in nums:
            numSet.add(num)
        for num in numSet:
            if (num - 1) not in numSet:
                start = num 
                length = 1
                while (num + length) in numSet:
                    length += 1
                    if length > longest:
                        longest = length
        return longest 
                        
                
            
        
            
            
                