class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])



        def dfs(row, col, perimeter):
            
            if row < 0 or col < 0 or col == cols or row == rows or grid[row][col]==0:
                return 1 + perimeter    
            if grid[row][col] == 2:
                return perimeter
            grid[row][col] = 2 
            perimeter = dfs(row+1, col, perimeter) + dfs(row-1, col, perimeter) + dfs(row, col+1, perimeter) + dfs(row, col-1, perimeter)
            return perimeter

        
        total = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    total = dfs(row, col, 0)
        return total