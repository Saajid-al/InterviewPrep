class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prev):
            if (r, c) in visit or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prev:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows-1, col, atl, heights[rows-1][col])

        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols-1, atl, heights[row][cols-1])
        res = []
        for row in range(rows):
            for col in range(cols):
                if (row,col) in atl and (row,col) in pac:
                    res.append((row,col))

        return res
