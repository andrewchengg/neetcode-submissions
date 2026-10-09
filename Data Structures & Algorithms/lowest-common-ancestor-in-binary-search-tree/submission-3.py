# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val == root.val:
            return root 
        if q.val == root.val:
            return root 
        if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
            return root 
        elif (p.val > root.val and q.val > root.val): #this means that p and q are always on the right side
            if root.right.val == p.val:
                return p
            elif root.right.val == q.val:
                return q
            return self.lowestCommonAncestor(root.right,p,q)
        elif (p.val < root.val and q.val < root.val): #this means that p and q are always on the left side
            if root.left.val == p.val:
                return p
            elif root.left.val == q.val:
                return q
            return self.lowestCommonAncestor(root.left,p,q)
            
        
                