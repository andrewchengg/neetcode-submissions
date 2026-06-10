class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        maximum = 0
        while right <= len(prices) - 1:
            if prices[left] >= prices[right]:
                left = right
                right = left + 1 
            elif prices[left] < prices[right]:
                diff = prices[right] - prices[left] 
                if diff > maximum: 
                    maximum = diff 
                right += 1 
        return maximum 
                    
                
