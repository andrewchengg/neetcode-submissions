class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0 
        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            if curr > best:
                best = curr
            if heights[left] == heights[right]:
                left += 1 
            elif heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
        return best 
            