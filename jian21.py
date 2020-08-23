from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i=0
        j=0
        while j < len(nums):
            if nums[j] % 2 == 0:
                j += 1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
                i += 1
        return nums


New = Solution()
New.exchange([1,2,3,4])