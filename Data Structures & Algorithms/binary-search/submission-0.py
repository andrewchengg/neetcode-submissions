class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1 
        while lo <= hi:
            middle = (hi + lo) // 2
            curr = nums[middle] 
            if curr == target: 
                return middle 
            elif curr > target: 
                hi = middle - 1
            else:
                lo = middle + 1 
        return -1 