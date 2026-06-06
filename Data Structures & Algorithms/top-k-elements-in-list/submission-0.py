from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        top_k = counter.most_common(k)
        top_k_keys = [key for key, _ in top_k]
        return(top_k_keys)  # ['a', 'b']

        
        