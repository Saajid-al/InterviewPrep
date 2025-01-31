class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        #bfs solution
        rows = len(grid)
        cols = len(grid[0])

        def isValid(row, col, visited):
            if row < 0 or col < 0 or row == rows or col == cols or grid[row][col] < 1 or (row, col) in visited:
                return False
            return True

        def bfs(row, col, maxFish):
            dir = [[0,1], [1,0], [-1, 0], [0,-1], [0,0]]
            queue = collections.deque()
            queue.append((row, col))
            visited = set()

            while queue:
                r, c = queue.popleft()
                for x,y in dir:
                    if isValid(r+x,c+y, visited):
                        queue.append((r+x, c+y))
                        visited.add((r+x, c+y))
                        maxFish += grid[r+x][y+c]
            return maxFish

        maxFishy = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0:
                    maxFishy = max(maxFishy, bfs(row, col, 0))

        return maxFishy



