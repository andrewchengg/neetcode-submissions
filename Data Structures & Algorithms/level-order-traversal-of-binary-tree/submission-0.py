# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        result = []
        queue.append(root)
        while queue:
            snapshot = len(queue)
            temp_result = []
            for i in range(snapshot):
                curr = queue.popleft()
                temp_result.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            result.append(temp_result)
        return result
            

             