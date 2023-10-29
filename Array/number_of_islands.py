class Solution(object):
    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])

        grid[r][c] = '0'
        if (r - 1 >= 0 and grid[r-1][c] == '1'):
            self.dfs(grid, r - 1, c)
        if (r + 1 < nr and grid[r+1][c] == '1'):
            self.dfs(grid, r + 1, c)
        if (c - 1 >= 0 and grid[r][c-1] == '1'):
            self.dfs(grid, r, c - 1)
        if (c + 1 < nc and grid[r][c+1] == '1'):
            self.dfs(grid, r, c + 1)

    def numIslands(self, grid):
        nr = len(grid)
        if not nr:
            return 0
        nc = len(grid[0])

        islsum = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    islsum += 1
                    self.dfs(grid, i, j)
        return islsum