# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        r_l = root.left
        r_r = root.right

        root.left = r_r
        root.right = r_l

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root