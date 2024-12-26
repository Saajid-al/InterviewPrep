class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        PacificSet = set()
        AtlanticSet = set()

        def dfs(row, col, visitSet, previous):
            if (row, col) in visitSet or row < 0 or col < 0 or row ==rows or col == cols or heights[row][col] < previous:
                return

            visitSet.add((row, col))
            dfs(row+1, col, visitSet, heights[row][col])
            dfs(row-1, col, visitSet, heights[row][col])
            dfs(row, col+1, visitSet, heights[row][col])
            dfs(row, col-1, visitSet, heights[row][col])

        for row in range(rows):
            dfs(row, 0, PacificSet, heights[row][0])
            dfs(row, cols-1, AtlanticSet, heights[row][cols-1])

        for col in range(cols):
            dfs(0, col, PacificSet, heights[0][col])
            dfs(rows-1, col, AtlanticSet, heights[rows-1][col])
        

        coord = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in PacificSet and (row, col) in AtlanticSet:
                    coord.append((row,col))

        return coord
