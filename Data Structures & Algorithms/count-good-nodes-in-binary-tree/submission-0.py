# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesHelper(node, maxVal):
            if node is None:
                return 0

            res = 1 if node.val >= maxVal else 0

            val = max(node.val, maxVal)
            res += goodNodesHelper(node.left, val)
            res += goodNodesHelper(node.right, val)

            return res

        return goodNodesHelper(root, root.val)
            