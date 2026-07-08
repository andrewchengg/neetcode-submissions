class Solution:
    def isValid(self, s: str) -> bool:
        reference = {"(":")","{":"}","[":"]"}
        stack = [] 
        for i in s: 
            if i in reference:
                stack.append(i)
            else:
                if not stack or reference[stack[-1]] != i: 
                    return False
                stack.pop()
        return not stack
                
        
            