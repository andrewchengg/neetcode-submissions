class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        merged.append(intervals[0])
        print(merged)
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            merged_node = merged[-1]
            lb1, ub1 = merged_node[0], merged_node[1]
            lb2, ub2 = curr_interval[0], curr_interval[1]
            if ub1 < lb2: #they do not overlap
                merged.append(curr_interval)
            elif ub1 >= lb2: #they do overlap 
                merged.pop()
                upper = max(lb1,lb2,ub1,ub2)
                lower = lb1
                merged.append([lower, upper])
        return merged


        
        
    
    #what would make overlapping intervals end up next to each other? i think sorting by the lower bound of the interval would make all the intervals end up next to each other. then, for all those with the same starting lower bound, we are going to find the one with the highest upper bound, and then merge them. 