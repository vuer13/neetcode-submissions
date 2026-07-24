# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        
        if self.isSubtreeHelper(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    def isSubtreeHelper(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None and root is None:
            return True
        
        if root and subRoot and subRoot.val == root.val:
            return (self.isSubtreeHelper(root.left, subRoot.left) and 
                    self.isSubtreeHelper(root.right, subRoot.right))
        
        return False