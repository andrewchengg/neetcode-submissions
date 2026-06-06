class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {} #row: list[int]
        columns = {} #column: list[int]
        subbucket = {} 
        for i in range(9):
            rows[i] = []
            columns[i] = []
        for i in range(3):
            for j in range(3):
                subbucket[str(i) + str(j)] = []
        #Init the dictionary 
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                bucket = str(int(i/3)) + str(int(j/3))
                if item != ".":
                    if item in rows[i] or item in columns[j] or item in subbucket[bucket]:
                        return False
                    rows[i].append(item)
                    columns[j].append(item)
                    subbucket[bucket].append(item)
        return True 
        
        
                