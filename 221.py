from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * (col+1) for i in range(row+1)]
        for i in range(1,row+1):
            for j in range(1, col + 1):
                if matrix[i-1][j-1] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp

New = Solution()
New.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])