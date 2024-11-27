class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
            rows = len(grid1)
            cols = len(grid1[0])
            visited = set()

            def dfs(row, col):
                if row < 0 or col < 0 or row == rows or col == cols or grid2[row][col] != 1 or (row, col) in visited:
                    return True
                
                res = True
                if grid1[row][col] != 1:
                    res = False
                visited.add((row,col))
                res = dfs(row-1,col) and res
                res = dfs(row+1,col) and res
                res = dfs(row,col-1) and res
                res = dfs(row,col+1) and res
                return res

            subIslands = 0 
            for row in range(rows):
                for col in range(cols):
                    if grid2[row][col] == 1 and (row, col) not in visited and dfs(row, col):
                        subIslands +=1 
            return subIslands
    
s = Solution()
print(s.countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))