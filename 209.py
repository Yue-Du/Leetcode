from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        pre=0
        post=1
        summ=nums[pre]+nums[post]
        min_length=len(nums)
        while post<len(nums):
            while pre<post:
                while summ<s and post<len(nums):
                    post=post+1
                    summ+=nums[post]
                min_length=min(min_length,post-pre+1)
                summ = summ - nums[pre]
                pre+=1
        return min_length


New = Solution()
New.minSubArrayLen(7,[2,3,1,2,4,3])