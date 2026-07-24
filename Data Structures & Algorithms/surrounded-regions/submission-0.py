class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        directions = [(1, 0), (0 , 1), (-1, 0), (0 , -1)]

        def dfs(i, j):
            if (
                i < 0
                or j < 0
                or i >= m
                or j >= n
                or board[i][j] == 'V'
                or board[i][j] == 'X'
            ):
                return
            
            board[i][j] = 'V'
            for dx, dy in directions:
                x, y = i + dx, j + dy
                dfs(x, y)
        
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'V':
                    board[i][j] = 'O'
        