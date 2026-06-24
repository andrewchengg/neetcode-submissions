class Solution:
    def isValid(self, s: str) -> bool:
        reference = {"(":")","{":"}","[":']'}
        stack = []
        if len(s) % 2 == 1 or len(s) == 0: 
            return False 
        for char in s: 
            if char in reference:
                stack.append(char)
            else:
                if not stack or char != reference[stack[-1]]:
                    return False
                stack.pop()
        return not stack 