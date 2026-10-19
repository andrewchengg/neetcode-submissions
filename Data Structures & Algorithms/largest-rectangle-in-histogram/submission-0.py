class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []                                  # (start_index, height), increasing heights
        best = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                best = max(best, height * (i - idx))   # popped bar can't stretch past i
                start = idx                            # new bar stretches back under it
            stack.append((start, h))
        for idx, height in stack:                      # these reached the right edge
            best = max(best, height * (len(heights) - idx))
        return best

