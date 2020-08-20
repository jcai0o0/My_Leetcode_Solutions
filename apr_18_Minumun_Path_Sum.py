class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        y, x = len(grid), len(grid[0])
        sum = grid[0][0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    prev = 0
                elif row == 0:
                    prev = grid[0][col - 1]
                elif col == 0:
                    prev = grid[row - 1][col]
                else:
                    prev = min(grid[row - 1][col], grid[row][col - 1])

                grid[row][col] = prev + grid[row][col]
        return grid[y - 1][x - 1]