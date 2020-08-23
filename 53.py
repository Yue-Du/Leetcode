from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        res=nums[0]
        i=0
        while i < len(nums)-1:
            if dp[i]>0:
                dp[i+1]=dp[i]+nums[i+1]
            else:
                dp[i+1]=nums[i+1]
            res=max(res,dp[i+1])
            i+=1
        return res

New = Solution()
New.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])