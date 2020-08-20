class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    ans += 1
                    self.dfs(grid, x, y, n, m)
        return ans

    def dfs(self, grid, x, y, n, m):
        if x < 0 or y < 0 or x >= n or y >= m or grid[y][x] == '0':
            return
        grid[y][x] = '0'
        self.dfs(grid, x + 1, y, n, m)
        self.dfs(grid, x - 1, y, n, m)
        self.dfs(grid, x, y + 1, n, m)
        self.dfs(grid, x, y - 1, n, m)