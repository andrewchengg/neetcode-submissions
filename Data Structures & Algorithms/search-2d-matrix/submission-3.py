class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_lo = 0 
        outer_hi = len(matrix) - 1
        while outer_lo <= outer_hi: 
            outer_mid = (outer_lo + outer_hi) // 2
            curr_row: List[int] = matrix[outer_mid] #current row
            inner_lo = 0
            inner_hi = len(curr_row) - 1
            if target < curr_row[0]:
                outer_hi = outer_mid - 1
            elif target > curr_row[-1]: 
                outer_lo = outer_mid + 1
            else: 
                while inner_lo <= inner_hi:
                    inner_mid = (inner_lo + inner_hi) // 2 
                    curr_number = curr_row[inner_mid] 
                    if curr_number == target:
                        return True 
                    elif curr_number > target:
                        inner_hi = inner_mid - 1 
                    elif curr_number < target:
                        inner_lo = inner_mid + 1 
                return False 
        return False 
                
            
        
            
                    
                
            
            
            

        