class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        result = []
        for i in strs:
            bruh = sorted(i)
            clean = ''.join([char for char in bruh])
            if clean not in temp: 
                temp[clean] = []
            temp[clean].append(i)

        for value in temp.values(): 
            result.append(value)
        return result 
            
        
        
        
                
                