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
            toAppend = []

            for _ in range(lenQ):
                node = queue.popleft()

                if node:
                    toAppend.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if toAppend:
                result.append(toAppend)

        return result
