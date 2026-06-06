class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for x in nums:
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] = hashmap[x] + 1 
        for num in hashmap:
            if hashmap[num] > 1:
                return True
        return False

        
        


        