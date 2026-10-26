# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndex = 0
        inOrder = 0

        def dfs(maxValue):
            nonlocal preIndex, inOrder

            if preIndex >= len(preorder):
                return None
            if inorder[inOrder] == maxValue:
                inOrder += 1
                return None

            val = preorder[preIndex]
            node = TreeNode(val=val)

            preIndex += 1

            node.left = dfs(val)
            node.right = dfs(maxValue)

            return node

        return dfs(1001)