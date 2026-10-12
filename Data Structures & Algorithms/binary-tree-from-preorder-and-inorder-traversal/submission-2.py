# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndex = 0
        inIndex = 0

        def dfs(maxValue):
            nonlocal preIndex, inIndex

            if preIndex >= len(preorder):
                return None
            if inorder[inIndex] == maxValue:
                inIndex += 1
                return None

            value = preorder[preIndex]
            root = TreeNode(val=value)

            preIndex += 1
            root.left = dfs(value)
            root.right = dfs(maxValue)

            return root

        return dfs(1001)