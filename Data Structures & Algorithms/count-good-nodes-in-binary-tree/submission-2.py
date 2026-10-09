# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, max_seen) -> int:
            if not root:
                return 0
            if root.val >= max_seen:
                return helper(root.left, root.val) + helper(root.right, root.val) + 1
            else:
                return helper(root.left, max_seen) + helper(root.right, max_seen) 
        return helper(root,root.val)

            






        