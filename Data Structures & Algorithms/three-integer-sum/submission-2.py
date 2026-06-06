class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = sorted(nums)
        result = []
        for i in range(0, len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            target = -(r[i])
            while left < right: 
                if (r[left] + r[right]) == target:
                    temp = [r[i],r[left],r[right]]
                    if temp not in result: 
                        result.append([r[i],r[left],r[right]])
                    right -= 1 
                if (r[left] + r[right]) > target:
                    right -= 1 
                if (r[left] + r[right]) < target:
                    left += 1 
        return result 
                

                

            
            