class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pacific = set()
        atlantic = set()

        def dfs(i, j, ocean, prevHeight):
            if (
                i < 0 or
                j < 0 or 
                i >= m or
                j >= n or
                (i, j) in ocean or
                heights[i][j] < prevHeight
            ):
                return
            
            ocean.add((i, j))
            for dx, dy in directions:
                dfs(i + dx, j + dy, ocean, heights[i][j])

        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n - 1, atlantic, heights[i][n - 1])

        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m - 1, j, atlantic, heights[m - 1][j])

        result = []

        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])

        return result
