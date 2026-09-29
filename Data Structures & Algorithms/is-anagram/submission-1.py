class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def dict_creator(s: str):
            seen = {} 
            for i in s:
                if i not in seen:
                    seen[i] = 1
                else:
                    seen[i] += 1 
            return seen 
        return dict_creator(s) == dict_creator(t)
            
                
                
            