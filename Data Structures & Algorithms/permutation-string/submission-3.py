

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        for i in range(0, len(s2)-window_len+1): #steps through gaps 
            strng = s2[i:i+window_len]
            if sorted(strng) == sorted(s1):
                return True
        return False 
                
            
                