class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        dp = [[0] * col for _ in range(row)]

        # res = 0

        for i in range(col):
            dp[0][i] = int(matrix[0][i])
            # res = max(res, dp[0][i])

        for i in range(row):
            dp[i][0] = int(matrix[i][0])
            # res = max(res, dp[i][0])

        for i in range(1, row):
            for j in range(1, col):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    # res = max(res, dp[i][j])
        res = max(max(row) for row in dp)
        return res ** 2