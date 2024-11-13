from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #check if we encounter a 0. if all cells around are x or O,
        rows = len(board)
        cols = len(board[0])


        def capture(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col]!="O":
                return
            board[row][col] = "T"
            capture(row+1,col)
            capture(row-1,col)
            capture(row,col-1)
            capture(row,col+1)


        for row in range(rows):
            capture(row,0)
            capture(row, cols-1)
        for col in range(cols):
            capture(0,col)
            capture(rows-1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"
                
            
        