
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums: 
            if num not in seen: 
                seen[num] = 1 
            else:
                seen[num] += 1
        #building the initial dictionary
        buckets = defaultdict(list) #now we are going to build the dictionary where key = frequency, and value = list of distinct and unique numbers that match that frequency
        for value, frequency in seen.items():
            buckets[frequency].append(value) 
        result = [] 
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)
                print(result)
                if len(result) == k:
                    return result
            
        