from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col, path):
            if grid[row][col] == 0:
                return path
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] <= 0:
                return path
            else:
                path += dfs(row+1, col, path) or dfs(row-1, col, path) or dfs(row, col+1, path) or dfs(row, col-1, path) 
            
            
            



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0:
                    grid[row][col]=dfs(row, col, 0)
        return grid




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