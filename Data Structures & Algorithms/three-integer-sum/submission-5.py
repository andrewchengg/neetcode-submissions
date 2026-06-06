class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = sorted(nums)
        result = []
        for i in range(0, len(nums) - 2):
            if (r[i] == r[i-1]) and i > 0:
                continue 
            left = i + 1
            right = len(nums) - 1
            target = -(r[i])
            while left < right: 
                if (r[left] + r[right]) == target:
                    result.append([r[i],r[left],r[right]])
                    while (r[left] == r[left + 1] and left < len(r)-2):
                        left += 1
                    while (right > 1 and r[right] == r[right - 1]):
                        right -= 1
                    right -= 1
                    left += 1 
                if (r[left] + r[right]) > target:
                    right -= 1 
                if (r[left] + r[right]) < target:
                    left += 1 
        return result 
                

                

            
            