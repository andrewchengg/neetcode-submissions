class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def find_letter_count(s: str): 
            letter_count = {}
            for x in s:
                if x not in letter_count:
                    letter_count[x] = 1;
                else: 
                    letter_count[x] += 1 
            return letter_count
        if find_letter_count(s) == find_letter_count(t):
            return True
        else:
            return False
                
                
            