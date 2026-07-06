# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        result = []

        queue.append(root)

        while queue:
            lenQ = len(queue)
            lastNode = None
            for q in range(lenQ):
                node = queue.popleft()
                if node:
                    lastNode = node
                    queue.append(node.left)
                    queue.append(node.right)
            if lastNode:
                result.append(lastNode.val)

        return result