# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def goodNodesHelper(root, value):
            nonlocal count

            if root is None:
                return

            if root.val >= value:
                count += 1

            goodNodesHelper(root.left, max(value, root.val))
            goodNodesHelper(root.right, max(value, root.val))

        goodNodesHelper(root, root.val)
        return count