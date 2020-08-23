from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=1
        while i <=k:
            nums.insert(0,nums[-1])
            nums.pop()
            i = i + 1
        return nums


New = Solution()
New.rotate([1,2,3,4,5,6,7],3)