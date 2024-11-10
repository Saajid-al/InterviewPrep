class Solution:
    def dfs(self, grid, row,col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != "1":
            return
        grid[row][col] = "0"
        lst = [(row-1, col), (row+1, col) , (row, col+1), (row, col-1) ]
        for r, c in lst:
                self.dfs(grid, r, c)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.dfs(grid, row,col)
                    numIslands+=1 
        return numIslands
    

    
        

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
    
