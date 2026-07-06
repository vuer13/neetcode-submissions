# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        result = []

        queue.append(root)

        while queue:
            lenQ = len(queue)
            new_list = []
            for q in range(lenQ):
                node = queue.popleft()
                if node:
                    new_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if new_list:
                result.append(new_list)

        return result