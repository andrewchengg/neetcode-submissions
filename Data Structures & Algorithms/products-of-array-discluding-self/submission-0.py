class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = nums[:]
            temp.pop(i)
            result = 1
            for num in temp:
                result *= num
            res.append(result)
        return res
                