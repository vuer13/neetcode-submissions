# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(node):
            nonlocal result

            if node is None:
                return 0

            leftVal = max(dfs(node.left), 0)
            rightVal = max(dfs(node.right), 0)
            result = max(result, leftVal + rightVal + node.val)

            return node.val + max(leftVal, rightVal)

        dfs(root)
        return result