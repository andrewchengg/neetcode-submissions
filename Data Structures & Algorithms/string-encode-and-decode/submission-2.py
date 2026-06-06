class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        count = 0
        string_len = ""
        while count < len(s):
            while s[count] != "#":
                string_len += s[count]
                count += 1
            length = int(string_len)
            res.append(s[count+1:count+1+length])
            count = count + 1 + length
            string_len = ""
        return res 
                