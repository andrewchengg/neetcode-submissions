class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
    #0 represents water, and then i can assume that everything else on the edges is water
    #an island - connectin adjacent lands horizontall or vertically and is surrounded by water - probably just means that one island is a collective of ones.
    #my initial thinking is that once we hit a land node, then we keep iterating left, up, right, down until there is nothing left, and then i want to keep a seen set so that we do not repeat things, especially for land nodes
        self.max_j = len(grid[0])
        self.max_i = len(grid)
        result = 0 
        self.visited = set() #storing the coordinates
        def helper(grid, i, j) -> None:
            if (i,j) in self.visited:
                return
            if i < 0 or j < 0 or i >= self.max_i or j >= self.max_j:
                return
            if grid[i][j] == "0":
                return
            self.visited.add((i,j))
            helper(grid, i-1,j)
            helper(grid,i,j-1) 
            helper(grid,i+1,j)
            helper(grid,i,j+1)

        for j in range(len(grid[0])): #i-th index of row
            for i in range(len(grid)): #i-th index of column
                print(i,j)
                val = grid[i][j] #current value
                if (i,j) not in self.visited and val == "1":
                    helper(grid, i, j)
                    result += 1 
        
        
        return result
                

        
    #defining the helper as a recursive method, wherein the base case literally is when it hits water, it just returns 0 - output type is just int: 0,1 - 1 being that this node represnts the island
                



