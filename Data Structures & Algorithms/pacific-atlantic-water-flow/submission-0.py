class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.maxr = len(heights)
        self.maxc = len(heights[0])
        pacific = set()
        atlantic = set() 
        def helper(heights,r, c, visited) -> None:
            curr = heights[r][c]
            for nnr, nnc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = nnr + r, nnc + c 
                if nr >= 0 and nc >= 0 and nr < self.maxr and nc < self.maxc:
                    new_value = heights[nr][nc]
                    if curr <= new_value and ((nr,nc)) not in visited:
                        visited.add((nr,nc))
                        helper(heights, nr, nc, visited) #recursive call
        
        #pacific
        for pc in range(self.maxc):
            helper(heights, 0, pc, pacific)
            pacific.add((0,pc))
        for pr in range(self.maxr):
            helper(heights, pr, 0, pacific)
            pacific.add((pr,0))
        
        #atlantic 
        for ar in range(self.maxr):
            helper(heights, ar, self.maxc - 1, atlantic)
            atlantic.add((ar, self.maxc - 1))
        for ac in range(self.maxc):
            helper(heights, self.maxr -1, ac, atlantic)
            atlantic.add((self.maxr-1,ac))
        return [list(cell) for cell in (pacific & atlantic)]

    
        
            
                


        
            

        



#plan is running DFS on all the bordering cells, starting with the pacific borders. this gives us a list of all the cells that can reach the pacific. then we do the same for the atlantic and then we do a union of the two lists. 