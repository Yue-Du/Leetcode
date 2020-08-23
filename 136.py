from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i=0
        while i <len(nums):
            sum=0
            j = 0
            while j <len(nums):
                if nums[i]==nums[j]:
                    sum=sum+1
                j=j+1
            if sum >1:
                i=i+1
            else:
                return nums[i]


new = Solution()
new.singleNumber([2,2,1])

