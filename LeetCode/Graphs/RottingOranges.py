import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        time = 0
        freshO = 0

        # Count fresh oranges and initialize the queue with rotten ones
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    freshO += 1 
                elif grid[row][col] == 2:
                    q.append([row, col])

        # Directions for adjacent cells (right, left, down, up)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # BFS to rot adjacent fresh oranges
        while q and freshO > 0:
            time += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    # Check bounds and if the orange is fresh
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        q.append([new_row, new_col])
                        freshO -= 1
        
        return time if freshO == 0 else -1
def main():
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))


if __name__ == "__main__":
    main()