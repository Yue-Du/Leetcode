from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_n = 0
        for i in range(0, len(nums)+1):
            sum_n += i
        sum_nums = 0
        for num in nums:
            sum_nums += num
        return sum_n-sum_nums


New = Solution()
New.missingNumber([3,0,1])