from collections import Counter, defaultdict

# figuring out how one dict is a subset of another one 
def match(d1,d2):  
    for key in d1.keys():
        if d1[key] > d2[key]: 
            return False 
    return True 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0 
        res = ""
        freq = defaultdict(int)
        reference = Counter(t) #init a reference
        for right in range(len(s)):
            freq[s[right]] += 1 
            while match(reference, freq):
                if res == "" or (right - left + 1) < len(res):
                    res = s[left:right+1]
                freq[s[left]] -= 1 
                left += 1 
        return res 


#requirements is that EVERY character in t must be present in some substring
# in s. and our job is to find the shortest substring for that. 
# it doesnt mean that we are to find the exact match.. its more of just 
# the shortest substring 

#input: s-> full string, t-> the string of letters to be found in the substring
#output: shortest substring out of everything -> string variable to store that

#what is the validity condition 