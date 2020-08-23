class Solution:
    def beibao(self, nums: List[int], w: int) -> int:
        n=len(nums)
        dp = np.zeros((n,w))
        i= n-1
        while i>=0:
            j=0
            while j<=w:
                if j< nums[i][0]:
                    dp[i][j]=dp[i+1][i]
                else:
                    dp[i][j]=max(dp[i+1][j].dp[i+1][j-nums[i][0]]+nums[i][1])
                j = j + 1
            i=i-1



New = Solution()
New.beibao([[2,3],[1,2],[3,4],[2,2]],5)