from typing import List
'''class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length=len(nums)
        dp=[0]*length
        dp[0]=nums[0]
        res=dp[0]
        for i in range(0,length-1):
            if nums[i+1]>0:
                if dp[i]>0:
                    dp[i+1]=dp[i]*nums[i+1]
                else:
                    dp[i+1]=nums[i+1]
            elif nums[i+1]<0:
                if dp[i]<0:
                    dp[i+1]=dp[i]*nums[i+1]
                else:
                    dp[i+1]=nums[i+1]
            else:
                if dp[i]>0:
                    dp[i+1]=dp[i]
                else:
                    dp[i]=nums[i]
            res=max(res,dp[i+1])
        return res'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        premax=nums[0]
        premin=nums[0]
        curmax=nums[0]
        curmin=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            curmax=max(nums[i],premax*nums[i],premin*nums[i])
            curmin=min(nums[i],premax*nums[i],premin*nums[i])
            res=max(res,curmax,curmin)
            premax=curmax
            premin=curmin
        return res
        return res


New = Solution()
New.maxProduct([-4,-3,-2])