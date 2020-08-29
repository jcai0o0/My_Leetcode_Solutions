class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        if fresh == 0:
            return 0
        dirs = [(0,1), (0,-1), (-1,0), (1,0)]
        step = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for d in dirs:
                    nx, ny = x+d[0], y+d[1]
                    if nx < 0 or nx >= row or ny < 0 or ny >= col or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    q.append((nx, ny))
                    fresh -= 1
            step += 1
        if fresh != 0:
            return -1
        return step -1