from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            while left + 1 < right and nums[left] == nums[right]:
                left = left + 1
            med = (left + right) // 2
            if nums[med] == target:
                return True
            elif nums[med] < target:
                if target > nums[right] and nums[med] < nums[right]:
                    right = med
                else:
                    left = med
            else:
                if target < nums[left] and nums[med] > nums[left]:
                    left = med
                else:
                    right = med
        if nums[left] == target or nums[right] == target:
            return True
        else:
            return False


New = Solution()
New.search([1,2,1],1)
