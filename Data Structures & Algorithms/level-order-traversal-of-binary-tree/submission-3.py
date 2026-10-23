# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque([root])

        while queue:
            lenQ = len(queue)
            add = []
            for _ in range(lenQ):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    add.append(node.val)

            if add:
                result.append(add)

        return result