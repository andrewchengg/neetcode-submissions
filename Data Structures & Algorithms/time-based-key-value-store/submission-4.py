class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None: #aim for O(1) time for set() 
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else: 
            self.store[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str: #aim for O(logn) time for get() 
        if key not in self.store:
            return "" 
        else:
            lo, hi = 0, len(self.store[key]) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                curr = self.store[key][mid][1]
                if curr == timestamp:
                    return self.store[key][mid][0] #returns the value immediately
                elif curr > timestamp: #remember that timestamp == target
                    hi = mid - 1 
                elif curr < timestamp:
                    lo = mid + 1 
            if hi >= 0:
                return self.store[key][hi][0]
            else:
                return ""

        
