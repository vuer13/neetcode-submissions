# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = deque()

        queue.append(root)
        while queue:
            len_queue = len(queue)
            level = []
            for _ in range(len_queue):
                curr_node = queue.popleft()
                if curr_node:
                    level.append(curr_node.val)
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
            if level:
                result.append(level)

        return result