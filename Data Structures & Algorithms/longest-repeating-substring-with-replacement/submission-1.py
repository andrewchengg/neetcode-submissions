
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        window_counts = Counter()
        longest = 0
        for right in range(len(s)):
            window_counts[s[right]] += 1 
            while ((right - left + 1) - (max(window_counts.values()))) > k:
                window_counts[s[left]] -= 1 
                left += 1
            longest = max(longest, right - left + 1)
        return longest