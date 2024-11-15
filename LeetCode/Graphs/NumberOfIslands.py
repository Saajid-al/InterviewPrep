class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != "1":
                return
            else:
                grid[row][col] = "0"
                dfs(row+1, col) 
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)

        numIslands = 0 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    numIslands +=1 
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
    
