class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1_len = len(word1)
        w2_len = len(word2)
        dp = [[0 for i in range(w2_len+1)] for j in range(w1_len+1)]
        for i in range(1,w1_len+1):
            for j in range(1, w2_len+1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return w1_len + w2_len - 2* dp[w1_len][w2_len]


New = Solution()
New.minDistance("sea","eat")