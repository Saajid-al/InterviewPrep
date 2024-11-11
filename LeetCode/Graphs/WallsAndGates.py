from typing import List
import collections

from typing import List
import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = collections.deque()

        def addPath(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visit or grid[row][col] == -1:
                return
            visit.add((row, col))
            q.append([row, col])

        # Initialize queue with cells containing '0'
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        # Perform BFS
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addPath(r + 1, c)
                addPath(r - 1, c)
                addPath(r, c - 1)
                addPath(r, c + 1)
            dist += 1

def main():
    s = Solution()
    print(s.islandsAndTreasure([
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]))



if __name__ == "__main__":
    main()