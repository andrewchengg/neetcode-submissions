class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visited = set() #(i,j) storing the coordinates 
        self.max_i = len(grid)
        self.max_j = len(grid[0])
        result = 0
        def helper(grid, i, j) -> int:
            if i < 0 or j < 0 or i >= self.max_i or j >= self.max_j:
                return 0 
            if grid[i][j] == 0:
                return 0
            if (i,j) in self.visited:
                return 0
            if (i,j) not in self.visited: 
                self.visited.add((i,j))
                return helper(grid, i-1, j) + helper(grid, i+1, j) + helper(grid, i, j-1) + helper(grid, i, j+1) + 1
            else: 
                return helper(grid, i-1, j)+ helper(grid, i+1, j)+ helper(grid, i, j-1) + helper(grid, i, j+1)
        
        for i in range(self.max_i):
            for j in range(self.max_j):
                value = grid[i][j]
                if value == 1 and (i,j) not in self.visited:
                    total = helper(grid, i, j)
                    result = max(result, total)
        return result 

        

            
            
