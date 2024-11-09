from typing import List


class Solution:

    def dfs(self, board, word, row,col, idx):
        if idx>=len(word):
            return True
        if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0 or board[row][col] != word[idx]:
            return False
        letter = board[row][col]
        board[row][col] = ""
        found = self.dfs(board, word, row+1, col, idx+1) or self.dfs(board, word, row-1, col, idx+1) or self.dfs(board, word, row, col+1, idx+1) or self.dfs(board, word, row, col-1, idx+1)
        board[row][col] = letter
        return found


    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and self.dfs(board, word, row, col, 0):
                    return True
        return False




def main():
    s = Solution()
    s.exist([[3,4,5],[3,3,1]], word="ha")

if __name__ == "__main__":
    main()