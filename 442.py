from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[abs(nums[i])-1] *= -1
        res = []
        for j in range(len(nums)):
            if nums[j] > 0:
                res.append(j)
        return res


New = Solution()
New.findDuplicates([4,3,2,7,8,2,3,1])