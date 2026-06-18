# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root

        def getRight(curr, res):
            while curr.right:
                res.append(curr.val)
                curr = curr.right
            res.append(curr.val)
            if curr.left:
                new_res = getRight(curr.left)
                res = res + new_res
            return res
        
        return getRight(curr, res)