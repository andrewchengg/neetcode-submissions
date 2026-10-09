# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #base case
        if not root:
            return True
        def helper(root,upper=float("inf"),lower=float("-inf")):
            if not root:
                return True 
            curr = root.val
            if curr <= lower or curr >= upper:
                return False 
            return helper(root.right,upper,root.val) and  helper(root.left,root.val,lower)

        return helper(root)
        
                

    #recursion problem where we break the entire tree down into subtrees and we are essentially seeing if that subtree is valid or not 