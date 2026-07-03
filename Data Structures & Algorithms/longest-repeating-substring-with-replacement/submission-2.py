from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maximum = 0 
        left = 0 
        window = Counter()
        for right in range(len(s)):
            window[s[right]] += 1
            while ((right - left + 1) - max(window.values())) > k:
                window[s[left]] -= 1 
                left += 1 
            maximum = max(maximum, right - left + 1)
                
        return maximum 