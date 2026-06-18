# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # make q into a queue
        q = deque([root])

        # while there are elements in there
        while q:
            # initalize
            rightSide = None
            lenQ = len(q)
            
            # for all elements on the row 
            for i in range(lenQ):
                # pop left element
                node = q.popleft()
                # add left, right side and set element to rightside
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            # Once we are done going through the whole level, then checkout the right element
            if rightSide:
                res.append(rightSide.val)
        return res