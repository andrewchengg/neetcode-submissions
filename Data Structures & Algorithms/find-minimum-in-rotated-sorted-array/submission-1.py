class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        result = nums[hi]
        while lo <= hi:
            mid = (lo + hi) // 2 
            curr = nums[mid]
            if curr < result:
                result = curr
            maximum = nums[hi] #highest in the current range 
            if curr > maximum: 
                lo = mid + 1 
            elif curr <= maximum: 
                hi = mid - 1
        return result 
            
            
            
            

        

#in this case, rotation means moving the last element to the front 
#we are given an array of length: n, which was originally in sorted ascending order
#and then it has become rotated between any number between 1 and n times, so it got shuffled, but still somewhat retains an ascending order with a breakage in the middle.
#my task is to find the min element of the array in O(logN) time. 

#first, is the base case wherein its just fully sorted from the start. but then how do we know if its just fully sorted or not. if we iterate through the entire list, then its just going to be O(n). 

#perhaps instead of taking in a case-wise basis, there must be something to do with the binary search and finding the minimum number. 

#a minimum is a minimum when the both numbers on the left and right must necessarily be bigger than the middle number. 

123456
612345
561234
456123
345612
234561