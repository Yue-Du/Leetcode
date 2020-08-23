from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = len(nums) + 1
        for j in range(len(nums)):
            if abs(nums[j]) <= len(nums) and abs(nums[j]) > 0 and nums[abs(nums[j]) - 1] > 0:
                nums[abs(nums[j]) - 1] *= -1
        for k in range(len(nums)):
            if nums[k] > 0:
                return k + 1
        nums.sort()



New = Solution()
New.firstMissingPositive([1,2,0])