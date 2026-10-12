from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        queue = deque()
        self.max_i = len(grid)
        self.max_j = len(grid[0])
        fresh_count = 0 
        for i in range(self.max_i):
            for j in range(self.max_j):
                curr = grid[i][j] 
                if curr == 2:
                    queue.append((i,j)) #queue contains the coordinates
                if curr == 1:
                    fresh_count += 1 
        visited = set()
        counter = 0
        while queue and fresh_count: #while queue and there are still fresh oranges
            snapshot = len(queue)
            counter += 1 
            print(counter)
            for _ in range(snapshot):
                curr = queue.popleft() #pops out the first node in the queue 
                i, j = curr[0], curr[1] 
                for nr, nc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + nr, j + nc 
                    if ni >= 0 and nj >= 0 and ni < self.max_i and nj < self.max_j: 
                        if grid[ni][nj] == 1 and (ni,nj) not in visited:
                            visited.add((ni,nj))
                            queue.append((ni,nj))
                            fresh_count -= 1
        if fresh_count:
            return -1 
        return counter


                



        
        
        

        
        



    #0 is an empty cell 
    #1 is a fresh fruit
    #2 representing a rotten fruit 

    #plan is bfs on the nodes where val == 2. we start the queue with all nodes of == 2 