# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val : idx for idx, val in enumerate(inorder)}
        self.pre_index = 0

        def buildTreeHelper(l, r):
            if l > r:
                return

            val = preorder[self.pre_index]
            root = TreeNode(val)
            self.pre_index += 1

            middle = index_map[val]
            root.left = buildTreeHelper(l, middle - 1)
            root.right = buildTreeHelper(middle + 1, r)

            return root

        return buildTreeHelper(0, len(inorder) - 1)
