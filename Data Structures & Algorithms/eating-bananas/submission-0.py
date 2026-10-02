class Solution:
    
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_possible(k:int, h:int, piles:List[int]):
            total = 0 
            for num in piles:
                total += (num + k - 1) // k
            return total
        lo_possible: int = 1 
        hi_possible: int = max(piles)
        result = hi_possible
        # the range is from [1,25]
        while lo_possible <= hi_possible:
            mid = (hi_possible + lo_possible) // 2
            hours = check_possible(mid,h,piles)
            if hours <= h:
                result = mid 
                hi_possible = mid - 1
            elif hours > h: #exceeded. need to up it. 
                lo_possible = mid + 1 
        return result 
                
            
    
        
        


#and we have a set total number of hours which we cannot exceed
#if the number of banans in the pile is less than k, then we can just simply finish it but we cannot start eating bananas from another pile.
#we are supposed to find the minimum number k, number of bananas per hour

#if this is a binary search problem, then i suppose that we have the upper bound as the max number, and the lower bound as 1, which is the default minimum. then our binary search algorithm is basically just trying to find the right number between 
