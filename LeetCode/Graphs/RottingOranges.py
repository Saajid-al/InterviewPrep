import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = collections.deque()

        def checkRotten(row, col):
            if grid[row][col] == 1:
                

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    q.append([row, col])
                    visited.add((row,col))

    

        mins = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                



def main():
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))


if __name__ == "__main__":
    main()