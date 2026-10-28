class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        in_degrees = [[0 for _ in range(n)] for _ in range(m)]

        # Initialize the in_degrees
        for i in range(m):
            for j in range(n):
                for dx, dy in DIRECTIONS:
                    x, y = i + dx, j + dy
                    if (
                         x < 0 
                         or y < 0
                         or x == m
                         or y == n
                         or matrix[i][j] >= matrix[x][y]
                    ):
                        continue
                    in_degrees[x][y] += 1

        queue = deque()
        for i in range(m):
            for j in range(n):
                if in_degrees[i][j] == 0:
                    queue.append((i, j))

        longestLength = 0
        while queue:
            lenQ = len(queue)
            for _ in range(lenQ):
                i, j = queue.popleft()
                for dx, dy in DIRECTIONS:
                    x, y = i + dx, j + dy
                    if (
                         x < 0 
                         or y < 0
                         or x == m
                         or y == n
                         or matrix[i][j] >= matrix[x][y]
                    ):
                        continue
                    in_degrees[x][y] -= 1
                    if in_degrees[x][y] == 0:
                        queue.append((x, y))

            longestLength += 1

        return longestLength          
