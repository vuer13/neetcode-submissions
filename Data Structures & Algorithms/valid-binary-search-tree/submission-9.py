# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(lowerBound, upperBound, node):
            if node is None:
                return True
            
            if (node.val <= lowerBound) or (node.val >= upperBound):
                return False
            
            return (valid(lowerBound, node.val, node.left)) and (valid(node.val, upperBound, node.right))

        return valid(float('-inf'), float('inf'), root)