from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def isLandCell(grid,i,j):
            return True if grid[i][j] == 2147483647 else False 
        queue = deque()
        self.max_i = len(grid)
        self.max_j = len(grid[0])
        for i in range(self.max_i):
            for j in range(self.max_j):
                if grid[i][j] == 0:
                    queue.append((i,j)) #queue should contain the coordinates so that we can find out who the neighbors are and have this information on hand 

                    #the "ripples" should be coming from the treasures as that is where we are measuring the distance from, and not the lands. 
        counter = 0
        while queue: #now the queue contains treasures only and we are doing like a ripple effect sort of thing 
            snapshot = len(queue)
            counter += 1 
            for _ in range(snapshot):
                curr = queue.popleft()
                i, j = curr[0], curr[1]
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + dr, j + dc 
                    if ni >= 0 and nj >= 0 and ni < self.max_i and nj < self.max_j and isLandCell(grid,ni,nj):
                        grid[ni][nj] = grid[i][j] + 1 
                        queue.append((ni,nj))
                


        



