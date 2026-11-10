# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We want to return a list of the values of the right most node at each level
        # Assumptions:
        # Number can be any number
        # root is a valid tree
        # Nothing returns Nothing
        
        # Thoughts so far:
        # In terms of getting nodes, we can do a couple of things:
        # DFS, BFS
        # Pre-order traversal
        # In-order traversal
        # Post-order traversal
        # Level-order traversal
        # I think that we can either do a DFS or BFS
        # For a BFS, we can go level by level, and at each level take the right most node
        # For a DFS, we can check the right side first, and see if it exists
        # - if so, take that node
        # - if not, look at its left node (since that will be the first exposed node)

        # Let's do a DFS for practice reasons
        # So DFS, we need to somehow check 
        # 1. what level are we at?
        # 2. have we checked this level for its right most node?
        # 3. If not, what do we do?

        # We can see that we need to traverse the RIGHT NODE first at minimum
        # If nothing is found there, then move onto the next
        # We need to keep track of the depth of the tree, and ensure we've seen every 
        # node there is on a level

        """
        result = []

        def dfs(node, level):
            if node is None:
                return

            if level == len(result):
                result.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result
        """

        # Now for a BFS, we need to look level by level, and only take the right node

        result = []

        if root is None:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            lenQ = len(queue)
            lastNode = None
            for _ in range(lenQ):
                node = queue.popleft()
                if node:
                    lastNode = node
                    queue.append(node.left)
                    queue.append(node.right)
            if lastNode:
                result.append(lastNode.val)

        return result
