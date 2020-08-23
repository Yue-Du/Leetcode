from typing import List
'''class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        i, count = 1, 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                    i -= 1
            else:
                count = 1
            i += 1

        return len(nums)'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        cnt=1
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                cnt=cnt+1
                if cnt>2:
                    nums.pop(i+1)
                    i=i-1
            else:
                cnt=1
            i=i+1
        return len(nums)


New = Solution()
New.removeDuplicates([1,1,1,2,2,3])