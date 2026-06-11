class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0,1 
        temp = {}
        maximum = 1
        temp[s[left]] = 0
        while right < len(s):
            if s[left] != s[right]:
                if s[right] not in temp:
                    temp[s[right]] = right
                    maximum = max(maximum, len(temp))
                    right += 1 
                else: 
                    left = temp[s[right]] + 1
                    right = left + 1
                    temp.clear()
                    temp[s[left]] = left
            else:
                left += 1
                right +=1 
        return maximum

                
                
                
        