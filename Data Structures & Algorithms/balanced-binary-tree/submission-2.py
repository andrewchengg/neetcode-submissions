# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.balanced = True
        def helper(root):
            if not root:
                return 0 
            left = helper(root.left)
            right = helper(root.right)
            if abs(left - right) > 1:
                self.balanced = False
            height = max(left, right) + 1
            return height
        helper(root)
        return self.balanced