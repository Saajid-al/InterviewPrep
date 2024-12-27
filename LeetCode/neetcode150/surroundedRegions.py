class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        def dfs(row, col):
            if row < 0 or col < 0 or row == rows or col == cols or board[row][col] != "O":
                return 
            
            board[row][col] = "T"

            dfs(row+1,col) 
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols-1)
        for col in range(cols):
            dfs(0, col)
            dfs(rows-1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"