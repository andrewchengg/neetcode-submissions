# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque() 
        levels_result = [] #list that stores the level-by-level traversal
        queue.append(root)
        while queue:
            snapshot = len(queue) 
            temp = []
            for i in range(snapshot):
                curr_node = queue.popleft() 
                temp.append(curr_node.val) 
                if curr_node.left: queue.append(curr_node.left)
                if curr_node.right: queue.append(curr_node.right)
            levels_result.append(temp) #appends the list of nodes in X level
        #List[List[int]] 
        final_result = [] 
        for level in levels_result:
            final_result.append(level[-1])
        return final_result



            

    
    