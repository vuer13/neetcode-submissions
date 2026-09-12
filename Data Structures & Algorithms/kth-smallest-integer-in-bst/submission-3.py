# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = root.val
        count = k

        def dfs(node):
            nonlocal result, count

            if node is None:
                return
            
            dfs(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                result = node.val
                return
            dfs(node.right)

        dfs(root)
        return result
