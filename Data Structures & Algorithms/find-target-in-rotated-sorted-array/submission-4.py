class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            curr = nums[mid]
            lowest = nums[lo]
            highest = nums[hi]
            if curr == target:
                return mid
            if lowest > curr: #then this must mean that mid to hi is sorted. so binary search mid to hi
                if target > curr and target <= highest:
                    lo = mid + 1
                else:
                    hi = mid - 1 
            elif lowest < curr: # this means that lowest to mid must be sorted. 
                if target >= lowest and target < curr:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif lowest == curr:
                lo = mid + 1
            
        return -1
            
#i think one of the main things to take note of is that there are two chunks of sorted numbers
#the question is more about how can we differentiate between the two sorted chunks 
#its always about the current number in relation to the target number, and figuring out if the target number is in the right chunk or not 
123456
612345
561234
456123
345612 
234561
