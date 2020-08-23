from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)
        for i in range(cnt):
            nums.remove(0)
            nums.append(0)
        return nums


New = Solution()
New.moveZeroes([0,1,0,3,12])