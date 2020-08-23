from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        max_len=1
        dp[0]=1
        i=0
        while i <len(nums)-1:
            if nums[i+1]<=nums[i]:
                dp[i+1]=1
            else:
                dp[i+1]=1+dp[i]
            max_len=max(max_len,dp[i+1])
            i+=1
        return max_len


New = Solution()
New.lengthOfLIS([10,9,2,5,3,7,101,18])