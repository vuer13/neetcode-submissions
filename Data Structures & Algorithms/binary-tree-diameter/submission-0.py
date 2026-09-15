# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def diameterOfBinaryTreeHelper(node):
            nonlocal result

            if node is None:
                return 0

            left = diameterOfBinaryTreeHelper(node.left)
            right = diameterOfBinaryTreeHelper(node.right)

            result = max(result, left + right)

            return 1 + max(left, right)

        diameterOfBinaryTreeHelper(root)
        return result
