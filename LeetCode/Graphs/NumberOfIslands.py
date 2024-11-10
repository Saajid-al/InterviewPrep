class Solution():
    
    def numIslands(self, grid):
        
        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    self.dfs(grid, row,col)
                numIslands+=1 
        return numIslands
    
    def dfs(self, grid, row,col):
        grid[row][col] = "0"
        lst = [(row-1, col), (row+1, col) , (row, col+1), (row, col-1) ]
        for r, c in lst:
            if grid[r][c] == "1" or r >= 0 or c >= 0 or r <= len(grid) or c <= len(grid[0]):
                self.dfs(grid, row, col)
    
        


def main():
    s = Solution()
    print(s.numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]))

if __name__ == "__main__":
    main()
    
