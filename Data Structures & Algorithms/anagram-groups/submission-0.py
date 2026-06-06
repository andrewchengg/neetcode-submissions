class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}
        def string_converter(string):
            return ''.join(sorted(string))
        
        for string in strs: 
            key = string_converter(string)
            if key not in hashmap:
                hashmap[key] = [string]
            else: 
                hashmap[key].append(string)
        return list(hashmap.values())
            

            
                
                