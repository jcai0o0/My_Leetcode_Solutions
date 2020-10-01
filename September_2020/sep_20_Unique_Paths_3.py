class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        vis = [[0 for _ in range(col)] for _ in range(row)]

        def dfs(i, j, step):
            if grid[i][j] == 2:
                if step == 0:
                    return 1
                else:
                    return 0
            vis[i][j] = 1
            step -= 1
            num1, num2, num3, num4 = 0, 0, 0, 0
            if i != 0 and vis[i - 1][j] == 0 and grid[i - 1][j] != -1:
                num1 = dfs(i - 1, j, step)
            if i != row - 1 and vis[i + 1][j] == 0 and grid[i + 1][j] != -1:
                num2 = dfs(i + 1, j, step)
            if j != 0 and vis[i][j - 1] == 0 and grid[i][j - 1] != -1:
                num3 = dfs(i, j - 1, step)
            if j != col - 1 and vis[i][j + 1] == 0 and grid[i][j + 1] != -1:
                num4 = dfs(i, j + 1, step)
            vis[i][j] = 0
            step += 1
            return num1 + num2 + num3 + num4

        step = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    p, q = i, j
                if grid[i][j] == 0:
                    step += 1
        return dfs(p, q, step + 1)